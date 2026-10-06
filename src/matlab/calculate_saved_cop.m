function result = calculate_saved_cop(heatFile, powerFile)
%CALCULATE_SAVED_COP Integrate saved useful-heat and input-power time series.
%   R = CALCULATE_SAVED_COP(QFILE, PFILE) reads each file's variable 'ans'.
%   Both must be scalar timeseries with Time in seconds and Data in watts.
%   Returns usefulHeat_J, inputEnergy_J and cop_energy_ratio (dimensionless).
%   Requires MATLAB only. No simulation runs and no files are written.
%
%   Preserves the original COP_Calc.m equation: trapz(Qtime,Q)/trapz(Ptime,P).
%   This is an energy ratio, not the arithmetic mean of instantaneous COP.
%   Caller must establish the source scenario, units and measured power boundary.
%   The original files do not establish those facts merely through filenames.
%   Signed data are preserved. This function does not clip or resample signals.
%   No runtime success is claimed; see docs/verification.md.

arguments
    heatFile (1,1) string
    powerFile (1,1) string
end
q = load_series(heatFile);
p = load_series(powerFile);
qtime = q.Time(:);
ptime = p.Time(:);
assert(abs(qtime(1) - ptime(1)) < 1e-9 && abs(qtime(end) - ptime(end)) < 1e-9, ...
    'Project:UnequalDuration', 'Heat and power must cover the same time interval.');
qint = trapz(qtime, q.Data(:));
pint = trapz(ptime, p.Data(:));
assert(pint > 0, 'Project:NonpositiveInputEnergy', 'Integrated input energy must be positive.');
result = struct('usefulHeat_J', qint, 'inputEnergy_J', pint, ...
    'cop_energy_ratio', qint / pint);
end

function series = load_series(filename)
assert(isfile(filename), 'Project:MissingFile', 'Missing MAT file: %s', filename);
data = load(filename, 'ans');
assert(isfield(data, 'ans') && isa(data.ans, 'timeseries'), ...
    'Project:WrongFormat', 'Expected a timeseries variable named ans in %s.', filename);
series = data.ans;
assert(isvector(series.Data) && numel(series.Time) == numel(series.Data), ...
    'Project:WrongShape', 'Time and Data must be equally sized vectors.');
assert(numel(series.Time) > 1 && all(isfinite(series.Time(:))) && ...
    all(isfinite(series.Data(:))) && all(diff(series.Time(:)) >= 0) && ...
    series.Time(end) > series.Time(1), ...
    'Project:InvalidSeries', 'Expected finite data over a positive, nondecreasing time interval.');
end
