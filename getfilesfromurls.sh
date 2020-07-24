file='all_links_file'

while read line; do

wget $line
echo "####"

done < $file
