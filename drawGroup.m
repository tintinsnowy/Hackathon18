function []= drawGroup(data,ls,jsonG)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
%outputArg1 = inputArg1;
%outputArg2 = inputArg2;
n = length(jsonG);
for i = 1:n
   IdSet = jsonG(i).Id;
   % find the in this group how many Tags are there.
   m = length(IdSet);
   count = jsonG.count;

   for j = 1:m
     Tag = IdSet(j);
     inx = find(ls==Tag);
     if(~isempty(inx))
        d = data(inx,2:4);
        scatter3(d(1),d(2),d(3));
        hold on;
        
     end
   end
  
end

end

