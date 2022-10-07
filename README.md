# overlap_check sdk
This repository contains a sample sdk for checking if in a given number of rectangles
any of them overlap or not. It gets a List of 2D rectangles defined with their lower-left and upper-right coordinates.

## Detailed Description of this SDK
This SDK (overlap_check) includes of following components

Component | Description |
--- |--- |
point | defines x and y coordinates of a given point |
do_overlap | verifies whether is there any overlap in a given set of 2D rectangles or not |


## Setup SDK locally

Clone the repository and run the following from the root folder

```
conda create -n <my env name> python=<ver> #ver > 3.6
conda activate <my env name>
python setup.py install

```
Test the installation by executing following on activate conda env

```
 python -c "from overlap_check import find_overlap"
```

## Sample check with two rectangles
```
 from overlap_check import find_overlap
 #Test Example; We can define as many as rectangles as our needs
 #Where 1st point is Lower Left coordinate & 2nd point is Upper Right coordinate
 #1st rect
 ll.append(find_overlap.Point(0, 0))
 ur.append(find_overlap.Point(4, 4))
    
 #2nd rect
 ll.append(find_overlap.Point(0, 5))
 ur.append(find_overlap.Point(10, 10))
 
 points_list = list(zip(ll, ur))
 
 if (find_overlap.do_overlap(points_list)):
    print("Rectangles Overlap")
 else:
    print("Rectangles Don't Overlap")
```

## Testing 
There is a sample jupyter notebook script which can also be used as template in order to test the SD.
It is located under:
```
 tests/overlap_checker.ipynb
```
