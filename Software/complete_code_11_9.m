% % Central coordinates
% x_0 =  287.5;
% y_0 = 318.5;
% 
% DMD_h = 720;
% DMD_w = 1280;
% 
% % scaling factor from DMD to CCD (b/c DMD/CCD = 5.4/5.86 = 0.922)
% scal = 0.9891;
% 
% % Lengths of lines
% x_crop = [554.1089,718.7266,20.8911,-143.7266];
% y_crop = [69.7843,755.0945,567.2157,-118.0945];
% 
% % Cropping : A,B,C,D
% height = 729;
% width = 1227;

load('calibration1.mat');
format short
% Affine transform
% load('calibration_dmd.mat');
% load('points.mat');
% Eliminate the translational part
T = tform.tdata.T;
T = [T(1,1) T(1,2) 0;T(2,1) T(2,2) 0;0 0 1.00];
% Tinv = [1.0986 -0.0394 0;0.0247 1.1077 0;0 0 1.0000];V2
tform = maketform('affine',T);     

[X,Y] = tformfwd(tform,p_p(:,1),p_p(:,2));
t_factor = [640-X(1),360-Y(1)];
V1 = [X,Y];
V2 = V1 + t_factor;

% final matrix
T(3,1) = t_factor(1);
T(3,2) = t_factor(2);

tform = maketform('affine',T);

disp('Calibration completed successfully. Please verify that V2 equals m_p.')
disp('...')
disp('...')
disp('...')
disp("For python code, use the matrix:")

% Adjustment added 09/21
% T(3,1) = T(3,1) + 82.0;
% T(3,2) = T(3,2) -57.0;
T = T';
disp(T)
%% Finding complete ROI
x = [0 1280];
y = [0 720];
ROI = [x',y'];
ROI = tforminv(tform,ROI(:,1),ROI(:,2));
disp('The ROI is defined by two coordinates of the rectangle:')
disp('Start_point:')
disp([ROI(1,1),ROI(1,2)])
disp('End_point:')
disp([ROI(2,1) ROI(2,2)])

%% Understanding how to find t_factor
% t_factor are the found as:
% 1. Display a circle centered at (640,360) on the DMD
% 2. Image it on the speckle camera
% 3. perform affine transformation on p_p coordinates with the translation set to (zero,zero)  
% 4. Lets call these the transformed coordinates: (X_sc,Y_sc)
% 5. Find the t_factor which is defined as (X_sc,Y_sc) + t_factor(x,y) = (640,360)

%% continue
% V3 = roipoly(zeros(720,1280),V2(:,1),V2(:,2));
% figure;
% imshow(V3);
% imwrite(V3,'DMD_sample.bmp');



