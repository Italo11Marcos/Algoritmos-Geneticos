function POPnovo = cruzamento(POP,xmin,xmax)
    
    [tamPOP, numVAR] = size(POP);
    POPnovo = POP; % Valores tempor�rios apenas para definir o tamanho de POPnovo
    
    for i = 1:tamPOP
        r = randperm(tamPOP,2);
        POPnovo(i,:) = (POP(r(1),:) + POP(r(2),:))./2;
%          if rand < 0.5
%               POPnovo(i,:) = POP(r(1),:) + rand(1,numVAR) - 0.5 .* (POP(r(2),:));
%          else
%              POPnovo(i,:) = POP(r(1),:);
    end
    
    POPnovo = max(POPnovo,xmin);
    POPnovo = min(POPnovo,xmax);
end