% Use this MATLAB script to identify the transform matrix for the
% LightCrafter projection onto the imaging plane. Instructions for use are
% on the FOIL Redmine under the Speckle Software wiki entry.

clear all; close all;


%% PART II - Capture the projected pattern using either the speckle 
% software or pylon Viewer (x64). Be sure to set the image dimensions as 
% 1040 x 1040px in the capture program.

%% PART III - Load in projected image and calculate the transform matrix

% Load the projected pattern image
[file, path] = uigetfile('*.*', 'Pick the projected image');
projected = imread([path file]);

% Load the actual image pattern
[file, path] = uigetfile('*.*','Pick the binary mask');
mask = imread([path file]);

initial_m_p = [640         360;
         340         160;
         940         160;
         340         560;
         940         560;
         640         160;
         640         560;
         340         360;
         940         360;
         200         240;
         200         480;
         500         240;
         500         480];
%          780         240;
%          780         480;
%         1080         240;
%         1080         480
%          ];
% initial_p_p =    [621.959793814433	744.712371134020;
% 360.998969072165	921.347422680412;
% 853.980412371134	939.809278350515;
% 382.953608247423	555.603092783505;
% 870.012743628186	579.458020989505;
% 609.485567010309	930.328865979381;
% 628.945360824742	563.586597938144;
% 368.982474226804	736.229896907217;
% 864.458762886598	754.691752577319;
% 240.747422680412	844.007216494845;
% 244.040729635183	624.790354822589;
% 499.213402061856	850.992783505155;
% 512.186597938144	631.945360824742;
% 728.739175257732	859.475257731959;
% 741.213402061856	643.421649484536;
% 968.743298969072	871.949484536082;
% 974.180659670165	653.725887056472;];

initial_p_p =    [621.959793814433	744.712371134020;
382.953608247423	555.603092783505;
870.012743628186	579.458020989505;
360.998969072165	921.347422680412;
853.980412371134	939.809278350515;
628.945360824742	563.586597938144;
609.485567010309	930.328865979381;
368.982474226804	736.229896907217;
864.458762886598	754.691752577319;
244.040729635183	624.790354822589;
240.747422680412	844.007216494845;
512.186597938144	631.945360824742;
499.213402061856	850.992783505155
];
% 728.739175257732	859.475257731959;
% 741.213402061856	643.421649484536;
% 968.743298969072	871.949484536082;
% 974.180659670165	653.725887056472];

   
% Use cpselect to identify control points in each image
[p_p, m_p] = cpselect(projected, mask,initial_p_p,initial_m_p, 'Wait', true);
% p_p([2,3,5,6,11,14,16,17],:) = [];
% m_p([2,3,6,16],:) = [];

User_input = input('Make sure everything looks good!');

% Generate the Affine transform matrix using these control points
tform = cp2tform(p_p, m_p,'affine');

% Print the transform to the command line
Tinv = tform.tdata.Tinv

clear initial_p_p initial_m_p
save('calibration1.mat');

format short
% Print formatted transform to the command line for copying to tform.txt
disp([num2str(Tinv(1,1)) ' ' num2str(Tinv(1,2)) ' ' num2str(Tinv(2,1)) ' ' ... 
    num2str(Tinv(2,2)) ' ' num2str(Tinv(3,1)) ' ' num2str(tform.tdata.Tinv(3,2))])

complete_code_11_9