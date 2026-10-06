function result = run_project(variant, action)
%RUN_PROJECT Inspect or simulate an unchanged academic model in an isolated copy.
%   INFO = RUN_PROJECT("r290_tuning", "inspect") reports saved settings.
%   RESULT = RUN_PROJECT("r290_tuning", "simulate") runs those saved settings.
%
%   Valid variants: r1234yf_snapshot, r290_final, r290_tuning.
%   Requires MATLAB, Simulink, Simscape and Simscape Fluids. Stateflow may be
%   needed for the tuning model's MATLAB Function blocks; verify locally.
%   No claim is made that these snapshots reproduce every case in the report.
%
%   Inputs: models/<variant>/*.slx, matching Parameters.m and speed MAT files.
%   Outputs: a new results/matlab/<unique run> folder and returned metadata;
%   simulation mode additionally saves simulation.mat. No source is overwritten.
%   Temperatures use degC, pressure MPa, speeds km/h or rpm as labeled in the
%   model. See docs/technical-summary.md for parameter and COP boundaries.
%
%   Parameter scripts run in a function workspace, so an inherited CLEAR
%   cannot erase the user's base workspace. Model settings are not rewritten.
%   The original scenario/example/plotting helpers are not invoked because
%   they refer to the upstream example topology rather than these snapshots.
%
%   Verification status: authored and statically reviewed; MATLAB execution
%   was unavailable during repository preparation (batch startup did not finish).

arguments
    variant (1,1) string {mustBeMember(variant, ...
        ["r1234yf_snapshot", "r290_final", "r290_tuning"])}
    action (1,1) string {mustBeMember(action, ["inspect", "simulate"])} = "inspect"
end

root = fileparts(fileparts(fileparts(mfilename('fullpath'))));
sourceDir = fullfile(root, 'models', variant);
modelName = 'ElectricVehicleThermalManagementWithHeatPump';
modelFile = fullfile(sourceDir, [modelName '.slx']);
parameterFile = fullfile(sourceDir, [modelName 'Parameters.m']);
assert(isfile(modelFile) && isfile(parameterFile), ...
    'Project:MissingModel', 'Supply the reviewed local model snapshot first; see models/README.md.');
assert(exist('Simulink.SimulationInput', 'class') == 8, ...
    'Project:MissingSimulink', 'Simulink is required.');
assert(~bdIsLoaded(modelName), 'Project:ModelAlreadyLoaded', ...
    'Close the currently loaded model with this name before selecting a snapshot.');

outputRoot = fullfile(root, 'results', 'matlab');
if ~isfolder(outputRoot)
    mkdir(outputRoot);
end
runDir = tempname(outputRoot);
mkdir(runDir);
copyfile(fullfile(sourceDir, '*'), runDir);
oldFolder = pwd;
oldPath = path;
originalFileGen = Simulink.fileGenControl('getConfig');
cleanup = onCleanup(@() restore_session(oldFolder, oldPath, originalFileGen, modelName));
cd(runDir);
addpath(runDir);
Simulink.fileGenControl('set', 'CacheFolder', fullfile(runDir, 'cache'), ...
    'CodeGenFolder', fullfile(runDir, 'codegen'), 'createDir', true);

parameters = read_parameters(fullfile(runDir, [modelName 'Parameters.m']));
load_system(fullfile(runDir, [modelName '.slx']));
scenario = [modelName '/Scenario/'];
info = struct('variant', variant, 'action', action, 'matlabVersion', version, ...
    'outputDirectory', runDir, 'stopTime_s', get_param(modelName, 'StopTime'), ...
    'ambientTemperature_degC', get_param([scenario 'Temperature [degC]'], 'Value'), ...
    'cabinTarget_degC', get_param([scenario 'Desired Temperature [degC]'], 'Value'), ...
    'batteryTarget_degC', get_param([scenario 'Battery Desired Temperature [degC]'], 'Value'));
disp(info);
save(fullfile(runDir, 'run-metadata.mat'), 'info', 'parameters');
if action == "inspect"
    result = info;
    return
end
assert(isfield(parameters, 'battery_T_init'), 'Project:MissingBatteryInitialTemperature', ...
    ['This snapshot references battery_T_init but its parameter script omits it. ' ...
     'Resolve the intended value before simulating; no value has been inferred.']);
simInput = Simulink.SimulationInput(modelName);
names = fieldnames(parameters);
for index = 1:numel(names)
    simInput = simInput.setVariable(names{index}, parameters.(names{index}));
end
simulationOutput = sim(simInput);
save(fullfile(runDir, 'simulation.mat'), 'simulationOutput', 'info', '-v7.3');
result = struct('info', info, 'simulationOutput', simulationOutput);
end

function parameters = read_parameters(filename)
% The source scripts contain scalar assignments; their CLEAR is isolated here.
run(filename);
names = who;
parameters = struct();
for index = 1:numel(names)
    value = eval(names{index});
    if isnumeric(value) && isscalar(value)
        parameters.(names{index}) = value;
    end
end
end

function restore_session(folder, originalPath, fileGen, modelName)
if bdIsLoaded(modelName)
    close_system(modelName, 0);
end
Simulink.fileGenControl('setConfig', 'config', fileGen);
path(originalPath);
cd(folder);
end
