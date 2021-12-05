function [POP,FX] = DE(POP,FX,xmin,xmax)
    [numPOP,numVAR] = size(POP);
    nPOP = POP;
    
    for i = 1:numPOP
        %Indivíduos aleatórios
        r = randperm(numPOP,3); %%r para DE/a/1/bin
        rr = randperm(numPOP,5); %rr para DE/a/2/bin
        j = randperm(numVAR);
        
        %Individuo da geração anterior //
        rOld = randperm(numPOP,1); %rOld para DE/a/1/bin
        rrOld = randperm(numPOP,1); %rrOld para DE/a/2/bin
        
        %Estratégia DE/rand/1/bin
        %nPOP(i,:) = POP(r(1),:) + rand * (POP(r(2),:) - POP(r(3),:));
        %Estratégia DE/best/2/bin
        %nPOP(i,:) = POP(rr(1),:) + rand * (POP(rr(2),:) - POP(rr(4),:)) + rand * (POP(rr(3),:) - POP(rr(5),:));
        %Estratégia DE/best/1/bin
        nPOP(i,:) = POP(rOld(1),:) + rand * (POP(r(3),:) - POP(rOld(1),:)) + rand * (POP(r(2),:) - POP(r(1),:));
        %Estratégia DE/rand/2/bin
        %nPOP(i,:) = POP(rrOld(1),:) + rand * (POP(rr(5),:) - POP(rrOld(1),:)) + rand * (POP(r(3),:) - POP(r(2),:));
        
        for d = 1:numVAR
            if ((rand <= 0.5) && (d ~= j(1)))
                nPOP(i,d) = POP(i,d);
            end            
        end
    end
    nPOP = max(nPOP,xmin);
    nPOP = min(nPOP,xmax);
    nFX = rastrigin(nPOP);
    
    for i = 1:numPOP
        if (nFX(i) < FX(i))
            POP(i,:) = nPOP(i,:);
            FX(i) = nFX(i);
        end
    end
    
end