cd ~/.vim/lly_source_code   &&
wget http://www.vim.org/scripts/download_script.php?src_id=17123 -O nerdtree.zip   &&
unzip nerdtree.zip  &&

mv doc ~/.vim  &&
mv nerdtree_plugin ~/.vim   &&
mv plugin ~/.vim    &&
mv syntax ~/.vim    
mkdir ~/.vim                                     #如已存在，则无需创建
                   如已存在，则无需创建
                         如已存在，则无需创建
 如已存在，则无需创建
cp ./doc/taglist.txt ~/.vim/doc &&
cp ./plugin/taglist.vim ~/.vim/plugin 
