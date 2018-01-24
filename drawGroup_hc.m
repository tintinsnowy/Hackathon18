
function []= drawGroup(data,ls,jsonG)

%UNTITLED2 Summary of this function goes here

%   Detailed explanation goes here

%outputArg1 = inputArg1;

%outputArg2 = inputArg2;

n = length(jsonG);
axis([292 5171 -963 950 -7 1200]);
hold on;
for i = 1:n
   IdSet = jsonG(i).Id;
   % find the in this group how many Tags are there.
   m = length(IdSet);
   count = jsonG(i).count;
    R = count/20000
    if R>1
        R=1
    end
    G = 1-R
    B = rand()
    % generate the same color for tags in the same group
   for j = 1:m
     Tag = IdSet(j);
     inx = find(ls==Tag)
     if(~isempty(inx))
        d = data(inx,2:4)
        for h = -7:15:d(3)/2+15
        scatter3(d(1),d(2),h,15,[R,G,B],'filled'); 
        scatter3(d(1),d(2),d(3)-h,15,[R,G,B],'filled'); 
        %plot3([d(1) d(1)],[d(2) d(2)],[-7 d(3)],'LineWidth',10);
        axis([292 5171 -963 950 -7 1200]);
        title('Spatial Distribution of Tags');
        xlabel('x');
        ylabel('y');
        zlabel('z');
        hold on;
        end
        pause(0.1);
     end
   end
   hold off;
  end   
end