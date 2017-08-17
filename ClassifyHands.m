min_row = 1;        %starting row to read from .csv (first cell is 0,0)
max_row = 1000000;   %last row to read from .csv
readfile = 'test.csv'   %name of input file
writefile = 'output.csv'%name of output file

input = csvread(readfile,min_row,0,[min_row,0,max_row,10]);

%create array to store output
s = zeros(max_row,2);
output = [ s];


current_row = 1;


%iterate through rows
while(current_row < (max_row + 1))
    %M is the current_row line of input matrix
    M = input(current_row,:);
    
    %store suits in matrix 'suits'
    suits = zeros(1,5);

    suits(1) = M(2);
    suits(2) = M(4);
    suits(3) = M(6);
    suits(4) = M(8);
    suits(5) = M(10);

    %store values in matrix 'values'
    values = zeros(1,5);

    values(1) = M(3);
    values(2) = M(5);
    values(3) = M(7);
    values(4) = M(9);
    values(5) = M(11);

    %find and classify the matching-values hands (pairs, threes, fours,
    %full-house)
    i = 1;
    j = 1;
    count = 1;
    first_rep = 0;
    second_rep = 0;
    first_val = 0;
    second_val = 0;
    result = 0;

    while i < 6
        count = 1;
        j = (i+1);

        while j < 6

            if(values(i) == values(j))
                %values(i)
                %values(j)
                count = (count + 1); 
            end

           j = (j + 1); 
        end

        if(count > 1)
           if(first_rep == 0)
               first_rep = count;
               first_val = values(i);
           else
               if(values(i) ~= first_val)
                   second_rep = count;
                   second_val = values(i);
                   break;
               end
           end
        end

        i = (i + 1);
    end


    % hand = 1, one pair
    if((first_rep == 2) && (second_rep == 0))
        result = 1;
    end


    % hand = 2, two pair
    if((first_rep == 2) && (second_rep == 2))
        result = 2;
    end

    % hand = 3, three of a kind
    if((first_rep == 3) && (second_rep == 0))
        result = 3;
    end

    if((first_rep == 0) && (second_rep == 3))
        result = 3;
    end

    % hand = 6, full house
    if((first_rep == 2) && (second_rep == 3))
        result = 6;
    end

    if((first_rep == 3) && (second_rep == 2))
        result = 6;
    end

    % hand = 7, four of a kind
    if((first_rep == 4) && (second_rep == 0))
        result = 7;
    end

    %find hands with all same suits (flush)
    if((suits(1) == suits(2)) && (suits(1) == suits(3)) && (suits(1) == suits(4)) && (suits(1) == suits(5)))
       result = 5; 
    end
    
    min = values(1);
    i = 1;

	%find consecutive-value hands (straight, straight flush)
	%note that Ace-high straight and royal flush are checked
	%for later
    while(i < 6)
        if(values(i) < min)
            min = values(i);
        end
        i = (i + 1);
    end

    min;

    i = 1;
    consecutive = 1;
    
    while(i < 5)
        j = 1;
        while (j < 6)
            if((values(j) == (min + i)))
                consecutive = (consecutive + 1);
                break;
            end
            j = (j + 1);
        end
        i = (i + 1);
    end

    %consecutive

	%if flush and straight, then straight flush
	%otherwise, straight
    if(consecutive == 5)
        if(result == 5)
            result = 8;
        else
            result = 4;
        end
    end

    i = 1;
    consecutive = 1;

	%check for ace-high straight, and royal flush
    if (min == 1)
        if ((result ~= 1) && (result ~= 2) && (result ~= 3) && (result ~= 6) && (result ~= 7))
            i = 1;
            consecutive = 1;

            while(i < 5)
                j = 1;
                while (j < 6)
                    if((values(j) == (i + 9)))
                        consecutive = (consecutive + 1);
                        break;
                    end
                    j = (j + 1);
                end
                i = (i + 1);
            end
        end
    end

	%consecutive
	%if flush and ace-high straight, then straight flush
    if(consecutive == 5)
        if(result == 5)
            result = 9;
        else
            result = 4;
        end
    end

    
    
    
    
    output(current_row,1) = M(1);
    output(current_row,2) = result;
    
    current_row = (current_row + 1);
end


csvwrite(writefile, output, 1, 0);

out = 'done'
