%take two matrices formatted as per the Kaggle guidelines for submission
%GeneticOut is the output matrix from genetic algorithm, MLOut is the
%output from the matlab ClassifyHands.m

i = 1;
errors = 0;
specific_error = zeros(10,10);

%generate a table of misclassified hands (assuming that MLOut accuracy 100%)
while (i < max_row + 1)
   if(MLOut(i,2) ~= GeneticOut(i,2))
       errors = (errors + 1);
       specific_error((MLOut(i,2)+1), (GeneticOut(i,2)+1)) = (specific_error((MLOut(i,2)+1), (GeneticOut(i,2)+1)) + 1);
   end
    i = (i + 1);
end

errors