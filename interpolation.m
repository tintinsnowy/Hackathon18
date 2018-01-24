function [x,y,z,vq]=interpolation(data) %test for interp3
%xq=290:15:5155;
%yq=-940:15:945;
%zq=0:15:1180;
xq=300:30:4500;
yq=-800:30:800;
zq=10:30:1100;
[x,y,z]=meshgrid(xq,yq,zq);
vq=griddata(data(:,1),data(:,2),data(:,3),data(:,4),x,y,z);
end