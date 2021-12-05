clearvars;
close all;
clc;

xmin = -5.12;
xmax = 5.12;
numPOP = 100;
numVAR = 5;
maxGER = 10000 / numPOP;

for i = 1:30
XF = linspace(xmin,xmax,100);
[X,Y] = meshgrid(XF,XF);

XF = [X(:) Y(:)];

POP = xmin + rand(numPOP,numVAR) * (xmax - xmin);
FX = calculaFX(POP);


    for g = 2:maxGER

%          POPnovo = cruzamento(POP,xmin,xmax);
%          POPnovo = mutacao(POPnovo,xmin,xmax);
%          %POPnovo = evolucao(POP);
%          FXnovo = calculaFX(POPnovo);
% 
%          POP = [POP; POPnovo];
%          FX = [FX; FXnovo];
% 
%          [POP, FX] = selecao(POP,FX,numPOP);

         [POP,FX] = DE(POP,FX,xmin,xmax);
    end
    vetor(i) = min(FX);
    
end
%Média dos 30 melhores resultados
media = mean(vetor)
%Desvio padrão
desvio_padrao = std(vetor)
%Melhor valor
best_value = min(vetor)
x = 1:30;
y = vetor;
plot(x,y);
title ('Rastrigin - DE/best/1/bin');
xlabel ('Execuções');
ylabel ('Fitness');
grid on;
