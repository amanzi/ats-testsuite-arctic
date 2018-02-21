%% Determine porosity and permeability curves for ATS
% Created by Mike O'Connor on 2.19.18 at 16:31

close all;
clear all;
clc;

R = cd;


%% Plot comsol porosity curve

% load porosity data points
load('C:\Users\mo8557\Dropbox\Imnavait UTexas Data\2016\Analysis\Matlab Flow Calculation Suite\porosity.mat');

zFit = 0:0.01:2;
phiFit = 10.^(-1.315.*zFit - 0.01968);

phi_min = ones(size(zFit)).*0.35;
plot(phiFit,-zFit,phi_min,-zFit);
hold all;

phi(24:50) = 0.2;
z(24:50) = linspace(0.5,2,27);
scatter(phi,-z);


