%matrix = csvread("PROCESSED_CSV.csv");
arg_list = argv ();
filename = arg_list{1};
matrix = csvread(filename);

figure(1)
plot(matrix(:,1), matrix(:,2))
figure(2)

dp_range = 1
n_div = 100 % number of divisions
[l,c] = size(matrix)
chunk_size = floor(l/n_div)

%inverting
for i = 1:l
    matrix(i,3) = 1/(matrix(i,2)) ;
endfor
plot(matrix(:,1), matrix(:,3))
figure(3)

max_v = max(matrix(:,3))
min_v = min(matrix(:,3))
avg = (max_v + min_v)/2


end_pos = 0;
chunks = [] % Start_pos, end_pos, mean minimum, bool keep?
for i = 1:n_div
  chunks(i,1) = start_pos = end_pos + 1;
  chunks(i,2) = end_pos = min([l,(start_pos+chunk_size)]);
  x = matrix(start_pos:end_pos,3);
  pks_x = findpeaks( x );
  chunks(i,3) = mean(pks_x);
endfor

valid_opt = []
for i = 1:l
    if matrix(i,3) > avg
       valid_opt(end+1) = matrix(i,3); 
    endif
endfor

med = mean(valid_opt)
dp = std(valid_opt)
cut_line = med - dp_range*dp

output_matrix = []
for i = 1:n_div
  if chunks(i,3) > cut_line
    output_matrix = [output_matrix;matrix( chunks(i,1):chunks(i,2),:)];
  endif
endfor

plot(output_matrix(:,1), output_matrix(:,2), " .b")
csvwrite("cut.csv", output_matrix)
pause




