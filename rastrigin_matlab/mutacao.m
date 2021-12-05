function POPnovo = mutacao(POPnovo,xmin,xmax)
    [tamPOP, numVAR] = size(POPnovo);
    
    for i = 1:tamPOP
          if (rand <= 1/numVAR) % Probabilidade de muta��o
              
              %%%substiuicao aleatoria
              POPnovo(i,:) = xmin + rand(1,numVAR) * (xmax - xmin);
              
          end
        
    end
    POPnovo = max(POPnovo,xmin);
    POPnovo = min(POPnovo,xmax);    
end
