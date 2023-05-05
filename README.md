# googleform_filler

### Notes: <br>
This is only a default setting of a specific google form.
If you want to have your own form automatically filled, you will need to find your id and change it.

### Setting:<br>
Selenium: the command here are used for version below 4.0, please type: <br>
To check the version of your selenium or if you have downloaded before:
```
pip3 freeze | grep selenium
```
if you have installed version 4.0 or after, please uninstall and install again
```
pip3 uninstall selenium

pip3 install selenium==3.9
```

Also the Chormedriver should be matching your chrome's version
Go to setting of chorme, and about Chrome, check your version and download the corresponding one.

### Controlling the distribution of selection

This require some basis knowledge of probability and statistic.<br>

Consider choices A and B, you want 80% of the people choose A and 20% choose B, then it is as same as 8 people choose A and 2 people choose B, among 10 people.<br>

Therefore, to control the number (not exact number, but around a percentage), you can use a random choice to genreate a value that is corresponding to a speicific answer.
```Python
import random

{
  'A':'Apple',
  'B':'Banana'
}

choice = random.choice(['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B'])

```

### XPath
To auto fill the answer, you should get the XPath of the button/ text. <br><br>

Step 1: <br>
Hover you cursor to the button or text space, right click and click inspect

![alt text](/images/inspect.png) <br><br>

Step 2:<br>
Then there will be a window showing the source file, and directly pointing to the line with respect to the button/ text space you hover on. <br><br>

Step 3:<br>
Right click, and click Copy, and select XPath. Then paste it back to the code, that would be the path corresponding to a specific choice of answer.

![alt text](/images/xpath.png) <br><br>

The reason of choosing xpath is that each xpath is unique, you can use class as a searching filter, but I don't find it works, so I use Xpath, and I find it works.<br><br>

Lastly, put it in the code, and do whatever you want together with the selenium method.<br>

```Python
station = {
    "1":'//*[@id="i5"]/div[3]/div',
    "2":'//*[@id="i8"]/div[3]/div',
    "3":'//*[@id="i11"]/div[3]/div',
    '4':'//*[@id="i14"]/div[3]/div', 
    '5':'//*[@id="i17"]/div[3]/div',
    '6':'//*[@id="i20"]/div[3]/div',
    '7':'//*[@id="i23"]/div[3]/div',
    '8':'//*[@id="i26"]/div[3]/div',
    '9':'//*[@id="i29"]/div[3]/div',
    '10':'//*[@id="i32"]/div[3]/div',
    '11':'//*[@id="i35"]/div[3]/div',
    '12':'//*[@id="i38"]/div[3]/div',
    '13':'//*[@id="i41"]/div[3]/div',
    '14':'//*[@id="i44"]/div[3]/div',
    '15':'//*[@id="i47"]/div[3]/div'
}
```

Be careful on the colon, as the xpat quoting the id is double colon, therefore you should use single colon to quote them.
