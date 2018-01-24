function[] = drawUndetected(data, ls, undetected)

l = length(undetected);
for i=1:l
   tag = undetected(i);
   index = find(ls==tag);
   
   if(~isempty(index))
       d = data(index, 2:4);
       star = scatter3(d(1), d(2), d(3),'k', '*');
       hold on;
   end
    
end

legend(star,"undetected RFID tags");
