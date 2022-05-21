function FX = rastrigin(POP)
    [numPOP, numVAR] = size(POP);

    if (numVAR < 2)
        fprintf('NÚMERO DE VARIÁVEIS INCORRETO\n');
        return;
    end
    
    FX = ones(numPOP,1) * 10 * numVAR;

    for d = 1:numVAR
        FX = FX + POP(:,d).^2 - 10*cos(2*pi*POP(:,d));
    end
    FX = FX;
end