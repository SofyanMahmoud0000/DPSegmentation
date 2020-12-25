### Segmentation of words with no spaces using DP (Dynamic Programming | Python)
In this repo, I have build a python project to do segmentation of words with no spaces using dynamic programming technique 

## How to run 
* Clone the project 
* Install python3 
* In the (input.json) file, you will put your input, for each input you will have two keys 
    * OriginalInput<number of input> : The original input or expected output 
        * if there is no original input -expected output- you must write the key and leave its value empty
    * NoSpaceInput<number of the input> : the input with no space, that you want to do the segmentation on it 
    * Example of the outptu: 
        ![Example](https://github.com/sofyanmahmoud0000/blob/master/images/Input.png)
* Run the file (Segmentation.py) using this command 
'''shell
python3 segmentation.py
''' 

* It will ask you about the number of input you want to select which you have assigned in the json file as we mentioned above 
    * Example
        * ![Example](https://github.com/sofyanmahmoud0000/blob/master/images/EnterInput.png)

## Output

It will show the original input, the expected output, the actual output, a list of the actual output and some statistics about the error, the number of words and character, etc..
![Example](https://github.com/sofyanmahmoud0000/DPSegmentation/blob/master/images/Output.png)

## Dataset 
* The dataset used in the project consists of (1/3) Million Most Frequent English Words on the Web and their frequency
* The size of the file of dataset is about (4 MB)
* The extension fo the file of dataset is (csv) 


## Built With

* [python 3](https://www.python.org/download/releases/3.0/) - Language used

## Development and support

If you have any questions on how to use this indexer, or have ideas for future development, please send me an e-mail to ***sofyan1020@gmail.com***.


## Author
[Sofyan Mahmoud](https://github.com/sofyanmahmoud0000) - Computer engineer