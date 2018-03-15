clc;clear;close all;


root = '/home/hyc/code/dehaze/dehaze_lab_tflearn/Comparisions/showDataset/showhazedata'
addpath(root)

savepath = '/home/hyc/code/dehaze/dehaze_lab_tflearn/Comparisions/showDataset/showpredict'
addpath(savepath)

imgnames=dir([root '/*' 'png']);

for ii=1:5%length(imgnames)
    disp(imgnames(ii).name)
    
    % read image
    %t = double(imread(depnames(ii).name))./255;
    
    % display image
    % figure, imshow(aaa, []);
    
    % save image
    % imwrite(arr,savename) ;
    
    % string concat
    % ['1','2','3']
    % sprintf('%s/%s',root,path)
    
    % zhu jie
    %{
        若干语句
    %}
    % 多行注释: 选中要注释的若干语句, 编辑器菜单Text->Comment, 或者快捷键Ctrl+R
    % 取消注释: 选中要取消注释的语句, 编辑器菜单Text->Uncomment, 或者快捷键Ctrl+T

    % tic用来保存当前时间，而后使用toc来记录程序完成时间。
    % tic
    %   operations
    % toc

end
