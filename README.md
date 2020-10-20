U are going to see some beatiful patterns which are mostly inspired from natures' art like branches, snowflake design, etc and some from mathematical artform.
And how we can construct them using very simple algorithm is just another exciting part of this demonstrstion. 
Let's get started!

# Fractals 
***The artform which we see everyday (in nature) but don't know what's the essence and what specific pattern it follows.***

Fractals are built with very complex pattern and they allow you to zoom in forever! It is basically a geometric figure which shows the same characteristics no matter how much you zoom in.
A rigorous definition:
"A fractal is an object or quantity that displays self-similarity, in a somewhat technical sense, on all scales. The object need not exhibit exactly the same structure at all scales, but the same "type" of structures must appear on all scales."-[Math-World](http://mathworld.wolfram.com/Fractal.html)

Fractals are typically hard to draw, because there is a concept which is deeply tight in them, recursion. When we talk about graphics and plotting we usually talk about pixels or vectors, but there is always a limit, fractals by definition are infinitely recursive. So when we want to plot one we should stop at some point, that's why we talk about "iterations". At each iteration the fractal becomes more and more complex, but at some point it is impossible to distinguish between to successive iterations (this happens when changes occur at individual pixel levels), so it is quite reasonable to stop there, sometimes it is quite clear what the shape is and we can stop even earlier.

## L-systems
An L-System is a way of representing recursive structures (such as fractals) as a string of characters, this is done by rewriting the string over and over. Again, the formal definition is the following:
- A Lindenmayer system, also known as an L-system, is a string rewriting system that can be used to generate fractals with dimension between 1 and 2. - [Math World](http://mathworld.wolfram.com/LindenmayerSystem.html)

Once we understand what an L-System is we can produce recursive structures, but before we are able to do that we need to understand what are the pieces we need. Every L-System has:
* An alphabet: The set of symbols the L-System is going to use.
* An axiom: The initial string for the generation.
* A set of production rules: These rules tells how each symbol should be replaced in the following iteration.
Here we will be using turtle to plot and *L-systems* to represent what we plot, we need to have some sort of relationship between those two.

The command string for L-systems will consists of 5 following symbols which will be guiding the turtle to move.
```
 F : Draw forward
 + : Turn right
 - : Turn left
 1 or 0: Draw forward
 A : Draw forward
 B : Move forward
 [ : Saving the current values for position and angle.
 ] : Restore the corresponding values for position and angle.
```
Ok we have done so much theory, let's hop on to the coding and implementation part which I bet would be most exciting.
### 3-Dragon Curve
```python
# 3 - Dragon curve

axiom = "FX+FX+FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 15 # TOP: 15
angle = 90
```
Code can be found [here](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/3_dragon_curve.py)

![Curve bla ](https://github.com/rodosingh/Tesellate-2020/blob/main/32-segment-curve.png)
### Levy-C curve
```python3
## Levy - C - curve

axiom = "F"
rules = {"F":"+F--F+"}
iterations = 16 # TOP: 16
angle = 45
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/levy_c_curve.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/Levy_c_curve.png)
### 32-Segment curve
```python3
## 32 segment curve
axiom = "F+F+F+F"
rules = {"F":"-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+"}
iterations = 2 # TOP: 3
angle = 90
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/32_segment_curve.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/32-segment-curve.png)
### Box-Fractal
```python3
# Box fractal

axiom = "F-F-F-F"
rules = {"F":"F-F+F+F-F"}
iterations = 5 # TOP: 6
angle = 90
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/box_fractal.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/box_fractal.png)
### Bransley-Fern(version 1)
Here we haven't use any L-systems string. Rather used the concepts as stated below:
```
First of all, the probability is calculated and the parameters are given as input to a function that performs matrix multiplication. 
Then the array is appended with new x and y points which are then converted into pixel coordinates by another function so that an image can be formed which can be plotted using matplotlib.
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/bransley_fern_realistic.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/bransley_fern_realistic.png)
### Bransley-Fern(version 2)
Again we haven't used any L-system algorithm to produce the following pattern.
Let's see what procedure we have followed.

The first point drawn is at the origin (x<sub>0</sub> = 0, y<sub>0</sub> = 0) and then the new points are iteratively computed by randomly applying one of the following four coordinate transformations:
```
ƒ1

xn + 1 = 0
yn + 1 = 0.16 yn.
```
This coordinate transformation is chosen 1% of the time and just maps any point to a point in the first line segment at the base of the stem. This part of the figure is the first to be completed during the course of iterations.
```
ƒ2

xn + 1 = 0.85 xn + 0.04 yn
yn + 1 = −0.04 xn + 0.85 yn + 1.6.
```
This coordinate transformation is chosen 85% of the time and maps any point inside the leaflet represented by the red triangle to a point inside the opposite, smaller leaflet represented by the blue triangle in the figure.

```
ƒ3

xn + 1 = 0.2 xn − 0.26 yn
yn + 1 = 0.23 xn + 0.22 yn + 1.6.
```
This coordinate transformation is chosen 7% of the time and maps any point inside the leaflet (or pinna) represented by the blue triangle to a point inside the alternating corresponding triangle across the stem (it flips it).

```
ƒ4

xn + 1 = −0.15 xn + 0.28 yn
yn + 1 = 0.26 xn + 0.24 yn + 0.44.
```
This coordinate transformation is chosen 7% of the time and maps any point inside the leaflet (or pinna) represented by the blue triangle to a point inside the alternating corresponding triangle across the stem (without flipping it).

The first coordinate transformation draws the stem. The second generates successive copies of the stem and bottom fronds to make the complete fern. The third draws the bottom frond on the left. The fourth draws the bottom frond on the right. The recursive nature of the IFS guarantees that the whole is a larger replica of each frond. Note that the complete fern is within the range −2.1820 < x < 2.6558 and 0 ≤ y < 9.9983.

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/bransley_fern.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/bransley_fern.png)

### Mandelbrot set

Mandelbrot set can be defined as a set of complex numbers which are generated by repeating the following equation again and again —
> Z<sub>n+1</sub> = Z<sub>n</sub>*Z<sub>n</sub> + C

To create a Mandelbrot fractal we repeat the above equation and vary C simultaneously within a box of complex plane: (-2, 1)x(-2, 1), till the absolute value or the magnitude of Z exceeds or equals to 4.
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/mandelbrot.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/mandelbrot.png)
### Julia Fractal
A Julia fractal can be defined as a subset of Mandelbrot fractal. While generating a Mandelbrot fractal, we changed the values of C and with Z<sub>0</sub> = 0. But for generating a Julia fractal the value of C is kept constant throughout the execution and Z is varied. For different values of C, different Julia fractals are formed.
> In the following image we have taken C = -0.42 + 0.6i

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/julia.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/julia.png)

### Cantor set
```python
# Cantor set

axiom = "A"
rules = {"A":"ABA", "B":"BBB"}
iterations = 10
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/cantor.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/cantor.png)
### Cross2
```python3
# Cross 2

axiom = "F+F+F+F"
rules = {"F":"F+FF++F+F"}
iterations = 5 # TOP: 6
angle = 90
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/cross2.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/cross2.png)
### Crystal
```python3
# crystal

axiom = "F+F+F+F"
rules = {"F":"FF+F++F+F"}
iterations = 5 # TOP: 6
angle = 90
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/crystal.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/crystal.png)
### Fractal Tree
```python3
# let's print the pattern
axiom = "X"
rules = {"X":"F+[[X]-X]-F[-FX]+X", "F":"FF"}
iterations = 6
angle = 25
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/fractal_plant.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/fractal-pattern.png)
### Hilbert Curve II
```python3
## Hilbert curve II

axiom = "X"
rules = {"X":"XFYFX+F+YFXFY-F-XFYFX", "Y":"YFXFY-F-XFYFX+F+YFXFY"}
iterations = 4 # TOP: 6
angle = 90
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/hilbert_curve.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/hilbert-curve-2.png)
### Peano-Gosper curve
```python3
# Peano-Gosper Curve
axiom = "FX"
rules = {"X":"X+YF++YF-FX--FXFX-YF+", "Y":"-FX+YFYF++YF+FX--FX-Y"}
iterations = 4 # TOP: 6
angle = 60
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/peano_gosper.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/peano_gosper.png)
### Pentaplexity
```python3
## Pentaplexity
axiom = "F++F++F++F++F"
rules = {"F":"F++F++F+++++F-F++F"}
iterations = 4 # TOP: 5
angle = 36
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/pentaplexity.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/pentaplexity.png)
### Quadratic-Snowflake
```python3
# Quadratic snow-flake

axiom = "F--F"
rules = {"F":"F-F+F+F-F"}
iterations = 5 # TOP: 6
angle = 90
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/quadratic_snow_flake.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/quadratic_snowflake.png)
### Rings
```python3
# Ring

axiom = "F+F+F+F"
rules = {"F":"FF+F+F+F+F+F-F"}
iterations = 4 # TOP: 4
angle = 90
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/ring.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/ring.png)
### Seirpinski-Arrowhead
```python3
# Serpienski - Arrowhead

axiom = "YF"
rules = {"X":"YF+XF+Y", "Y":"XF-YF-X"}
iterations = 8 # TOP: 10
angle = 60
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/seirpinski_arrowhead.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/seirpinski_arrowhead.png)
### Tiles
```python3
# Tiles
axiom = "F+F+F+F"
rules = {"F":"FF+F-F+F+FF"}
iterations = 4 # TOP: 4
angle = 90
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/tiles.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/tiles.png)

# Some more interesting patterns for you!
## Vibrating-Sphere
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/vibrate_circle.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/vibrating_sphere.png)
## Binary tree
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/binary_tree.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/binary_tree.png)

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/pattern2.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/pattern_2.png)

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/pattern6.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/pattern6.png)

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/pattern5.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/pattern5.png)

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/pattern4.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/pattern4.png)
![](https://github.com/rodosingh/Tesellate-2020/blob/main/pattern4_1.png)

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/pattern3.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/pattern3.png)
![](https://github.com/rodosingh/Tesellate-2020/blob/main/pattern3_1.png)

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/pattern2.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/pattern2.png)
