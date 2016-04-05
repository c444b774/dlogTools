mat = csvread("PROCESSED_CSV.csv");

tx_kill = 0.05
tx_accp = 0.9999
dp_range = 8

plot(mat(:,1), mat(:,2))
pause

do
  current = mat(:,2);
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
      if mat(k,2) <= line
	mat(k,2) = 0
      % tokeep(end+1) = k;
      endif
    endfor
  %mat = mat(tokeep,:);
  endif
until retest == 0


plot(mat(:,1), mat(:,2), ".b", mat(:,1), mat2, "-r" )
csvwrite("trimmed.csv", mat)
pause


