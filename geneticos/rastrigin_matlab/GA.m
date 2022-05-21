function nPOP = GA(POP,xmin,xmax)
    [numPOP,numVAR] = size(POP);
    nPOP = POP;
    
    for i = 1:numPOP
        r = randperm(numPOP);
        j = randperm(numVAR);
        
        nPOP(i,:) = POP(i,:) + (2 * rand - 0.5) * (POP(r(1),:) - POP(i,:));
        
        for d = 1:numVAR
            if (rand <= 0.2)
                nPOP(i,d) = nPOP(i,d) + 0.2 * (rand - 0.5) * (xmax - xmin);
            end            
        end        
    end
    nPOP = max(nPOP,xmin);
    nPOP = min(nPOP,xmax);
end