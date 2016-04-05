%matrix = csvread("PROCESSED_CSV.csv");
arg_list = argv ();
filename = arg_list{1};
matrix = csvread(filename);


tx_kill = 0.05 % %points will be killed at each iteration
tx_accp = 0.9999 % %Points that must to be at dp_range to acceptance
dp_range = 8

%plot(matrix(:,1), matrix(:,2))
%pause

do
  current = matrix(:,2);
  [l,c] = size(current)
  med = mean(current)
  dp = std(current)
  
  mat2 = current*0 + med;
  sorted = sort(current);
  maximum_value = sorted(end) %debug  
  retest = 0;
  
  max_value_for_accep = dp_range*dp + med %debug
  for accp_test = 1:l %Test how many dots are inside the range
    if sorted(accp_test) > (dp_range*dp+med)
      accp_test = accp_test % debug
      break
    endif
  endfor

  target_for_acceptation = l*tx_accp %debug
  if accp_test < l*tx_accp %If does not pass the test..
    killed = tx_kill*l 
    retest = 1
    
    line = sorted(l-floor(killed)+1)
    tokeep = [];
    for k = 1:l        %..kill "killed" biggest dots
      if matrix(k,2) > line
	matrix(k,2) = med;
      % tokeep(end+1) = k;
      endif
    endfor
  %matrix = matrix(tokeep,:);
  endif
until retest == 0


plot(matrix(:,1), matrix(:,2), ".b", matrix(:,1), mat2, "-r" )
csvwrite("trimmed.csv", matrix)
pause
pause



