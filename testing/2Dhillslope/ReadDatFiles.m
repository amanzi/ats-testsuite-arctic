%% Read ATS Hydrograph
% Created by Mike O'Connor on 9.28.17 at 11:59
% Description: this script reads a .dat file and plots it.

close all;
clear all;
clc;

R = cd;

filename = './test7/run4_25Sep17/surface_outlet_flux.dat';

read(filename);