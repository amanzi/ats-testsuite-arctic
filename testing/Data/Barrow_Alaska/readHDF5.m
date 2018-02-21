%% Plot HDF5 files

close all;
clear all;
clc;

% Add filename
file = '../Nome_Alaska/Seward-DayMet-1985_2016.h5';

% Determine data series within file
info = hdf5info(file);

l = length(info.GroupHierarchy.Datasets);

for i = 1:l
    data(:,i) = hdf5read(info.GroupHierarchy.Datasets(i));
    dataNames{i} = info.GroupHierarchy.Datasets(i).Name;
end

%dataNames