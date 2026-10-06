function tests = test_saved_cop
%TEST_SAVED_COP Synthetic dimensional and integration checks; no model required.
% Run: addpath('src/matlab'); results = runtests('tests/test_saved_cop.m');
% These tests have not been executed in the preparation environment.
tests = functiontests(localfunctions);
end

function testConstantPower(testCase)
directory = tempname;
mkdir(directory);
cleanup = onCleanup(@() rmdir(directory, 's'));
payload.ans = timeseries([2000; 2000; 2000], [0; 5; 10]);
save(fullfile(directory, 'heat.mat'), '-struct', 'payload');
payload.ans = timeseries([1000; 1000; 1000], [0; 5; 10]);
save(fullfile(directory, 'power.mat'), '-struct', 'payload');
r = calculate_saved_cop(string(fullfile(directory, 'heat.mat')), ...
    string(fullfile(directory, 'power.mat')));
verifyEqual(testCase, r.usefulHeat_J, 20000);
verifyEqual(testCase, r.inputEnergy_J, 10000);
verifyEqual(testCase, r.cop_energy_ratio, 2);
end
