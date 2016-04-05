arg_list = argv ();
filename = arg_list{1};
matrix = csvread(filename);

[l, c] = size(matrix);

acc = (matrix(l,1) - matrix(1,1))/l ; 
disp(acc) 

