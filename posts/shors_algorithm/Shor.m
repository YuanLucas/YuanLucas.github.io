clf
clear
clc
N=14351;
m=0:14351;
hfig=figure;

stem(m,abs(mod(m*28,N))<=100,'b')
xlabel('$$y$$','Interpreter','latex')
ylabel('$$|a_y|^2$$','Interpreter','latex')

figWidth=10;
figHeight=5;
set(hfig,'PaperUnits','inches');
set(hfig,'PaperPosition',[0 0 figWidth figHeight]);
fileout=['QFT'];
print(hfig,fileout,'-r300','-dpng');