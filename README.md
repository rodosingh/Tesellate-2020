U are going to see some beatiful patterns which are mostly inspired from natures' art like branches, snowflake design, etc and some from mathematical artform.
And how we can construct them using very simple algorithm is just another exciting part of this demonstrstion. 

Let's get started!

***The first and the second one are very special and are the best creations for us.***
# Math Sea-Hydra
This plot is that of a single equation with two parameter. Although it looks like a hydra because of limitations of plotter, the graph is actually that of a rose. It was devised by **Paul Nylander**. You can find a interactive version of this Nylander’s rose [here](https://demonstrations.wolfram.com/ARoseForValentinesDay/).

Sources: 

- [Nylander’s website](http://www.bugman123.com/Math/index.html)

- [Zhuanlan’s website](https://zhuanlan.zhihu.com/p/93160646)

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/hydra.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/sea_hydra.png)
# Tupper's self referential formula.
Although at first glance this may not seem anything special. What is really special is the way the above image is obtained. This is the set of points that satisfy the following equation in (x,y) plane:

> ![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7B2%7D%3C%5Cbigg%5Clfloor%20mod%5Cbigg%28%5Cbigg%5Clfloor%20%5Cfrac%7By%7D%7B17%7D%5Cbigg%5Crfloor2%5E%7B-17%5Clfloor%20x%5Crfloor-mod%28%5Clfloor%20y%5Crfloor%2C%2017%29%7D%2C%202%5Cbigg%29%5Cbigg%5Crfloor)

This is the **Tupper's self-referential formula** which visually represents itself when graphed at a specific location in the (x, y) plane. Moreover, if one graphs the set of points (x, y) in 0 ≤ x < 106 and k ≤ y < k + 17 for carefully chosen k than graph can represent any bitmap of 106*17 dimensions in particular **Tessallate 20 with the IISER Kolkata logo** in our case.
One cheat that we have done here is the method for finding "k". The k can be obtained by writing the string of 0’s and 1’s taken vertically in the bitmap to be plotted converted to decimal and then multiplies by 17.

For this specific example, k is the humongous number:

```math
k = 67902954172998279779148307035748543875626596626715618561774187298250934363549920526861826892045775471523420051461059352025730300728958258871827716521787586712381787510119167276708826565795256746434934552536649167561691076324207650135136161187337977520439136681142558385669897289470014091418155046364284809275257284325238561696967838276454959424074770534470832345336843136842298839488031465819970706806272288559418337139408254938926081268534150613103890536180137166904957677964324617241882919757702991732941427976984898637824
```

One can use the following [link](https://keelyhill.github.io/tuppers-formula/) to play with other patterns.

Also to print the self-referential formula of **Tupper's** itself take k as follows:
```math
k = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719
```

Sources: 

- [Wikipedia](https://en.wikipedia.org/wiki/Tupper%27s_self-referential_formula)

- [Numberphile (youtube)](https://www.youtube.com/watch?v=_s5RFgd59ao)

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/tesellate.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/tesellate.png)
# Fractals 
***The artform which we see everyday (in nature) but don't know what's the essence and what specific pattern it follows.***

Fractals are built with very complex pattern and they allow you to zoom in forever! It is basically a geometric figure which shows the same characteristics no matter how much you zoom in. They are common in nature and are found nearly everywhere. An example is broccoli. Every branch of broccoli looks just like its parent stalk. The surface of the lining of your lungs has a fractal pattern that allows for more oxygen to be absorbed. Such complex real-world processes can be expressed in equations through fractal geometry. Even to the everyday person, fractals are generally neat to look at even if you don't understand what a fractal is. But to a mathematician, it is a neat, neat subject area.

**Why are fractals important?**

- Fractals help us study and understand important scientific concepts, such as the way bacteria grow, patterns in freezing water (snowflakes) and brain waves, tree branches, clouds, the scattering of stars, waves on the sea, blossoming petals, or river tributaries, for example. Their formulas have made possible many scientific breakthroughs. Wireless cell phone antennas use a fractal pattern to pick up the signals better, and pick up a wider range of signals, rather than a simple antenna. Anything with a rhythm or pattern has a chance of being very fractal-like.

- Also these involve imaginary components in the unreal dimensions of i, j, k (![](https://latex.codecogs.com/gif.latex?%3D%20%5Csqrt%20-1), which cannot exist in the physical plane). What the fractal we see in art and in nature actually is is a projection of the invisible and intangible fractal itself. This points to the fact that natural phenomena are the projection on the physical plane (4 dimensions actually!) of an underlying reality which is at heart complex. It carries the philosophical meaning that the foundation of our observed reality is a multiple- and higher-dimensional underlying reality in a mathematical realm, including unreal components. An example of this is differential calculus, where the solutions for mundane equations very often invoke transcendental numbers like ![](https://latex.codecogs.com/gif.latex?%5Cpi) (3.14159...) and e (2.71828...), or even complex numbers involving i (![](https://latex.codecogs.com/gif.latex?%3D%20%5Csqrt%20-1)). Though the equations seem to involve "imaginary" numbers, in fact, they describe electromagnetic waves and many other real phenomena, where a component of the vibration is in another dimension at right angles to what we call physical reality.

****Originally the L-systems were devised to provide a formal description of the development of such simple multicellular organisms, and to illustrate the neighbourhood relationships between plant cells. Later on, this system was extended to describe higher plants and complex branching structures.**** - [Wiki](https://en.wikipedia.org/wiki/L-system#:~:text=Originally%20the%20L%2Dsystems%20were,plants%20and%20complex%20branching%20structures.)

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

A dragon curve is a recursive nonintersecting curve whose name derives from its resemblance to a certain mythical creature. It was first investigated by NASA physicists **John Heighway**, **Bruce Banks**, and **William Harter**. It can be construed iteratively by starting from a base segment, replacing each segment by 2 segments with a right angle and with a rotation of 45° alternatively to the right and to the left. You can find an animated video of the dragon curve in the [numberphile video](https://www.youtube.com/watch?v=NajQEiKFom4).

Sources:

- [Numberphile (youtube)](https://www.youtube.com/watch?v=wCyC-K_PnRY)

- [Wikipedia](https://en.wikipedia.org/wiki/Dragon_curve)

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
The Lévy C curve is a self similar fractal curve. You can find an animated video of its iteration [here](https://www.youtube.com/watch?v=iG17gOKlx14). Not only is its shape breathtaking, it has important mathematical properties. It belongs to the family of **Koch curves** which were one of the earliest fractals to be described.

Sources: 

- [Wikipedia](https://en.wikipedia.org/wiki/Lévy_C_curve)

- [Online Lévy curve generator](https://onlinemathtools.com/generate-levy-c-curve)

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

The first coordinate transformation draws the stem. The second generates successive copies of the stem and bottom fronds to make the complete fern. The third draws the bottom frond on the left. The fourth draws the bottom frond on the right. The recursive nature of the  [iterated function system](https://en.wikipedia.org/wiki/Iterated_function_system) (IFS) guarantees that the whole is a larger replica of each frond. Note that the complete fern is within the range −2.1820 < x < 2.6558 and 0 ≤ y < 9.9983.

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/bransley_fern.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/bransley_fern.png)

### Mandelbrot set
Mandelbrot set is important for chaos theory.

It can be defined as a set of complex numbers which are generated by repeating the following equation again and again —
> Z<sub>n+1</sub> = Z<sub>n</sub>*Z<sub>n</sub> + C

To create this we repeat the above equation and vary C simultaneously within a box of complex plane: (-2, 1)x(-2, 1), till the absolute value or the magnitude of Z exceeds or equals to 4.

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/mandelbrot.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/mandelbrot.png)
### Julia Fractal
A Julia fractal can be defined as a subset of Mandelbrot fractal. While generating a Mandelbrot fractal, we changed the values of C and with Z<sub>0</sub> = 0. But for generating a Julia fractal the value of C is kept constant throughout the execution and Z is varied. For different values of C, different Julia fractals are formed.
> In the following image we have taken C = -0.42 + 0.6i

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/julia.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/julia.png)
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

### L-system Bush
```python3
# Dense Bush

axiom = "VZFFF"
rules = {"V":"[+++W][---W]YV", "W":"+X[-W]Z", "X":"-W[+X]Z", "Y":"YZ", "Z":"[-FFF][+FFF]F"}
iterations = 12 # TOP: 6
angle = 20
```

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/dense_bushes.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/dense_bush.png)

### Cantor set
A Cantor set is a closed set in which every point is an accumulation point is also called a perfect set in topology, while a closed subset of the interval with no interior points is nowhere dense in the interval. Every point of the Cantor set is also an accumulation point of the complement of the Cantor set. - [Wiki](https://en.wikipedia.org/wiki/Cantor_set#:~:text=A%20closed%20set%20in%20which,complement%20of%20the%20Cantor%20set.)

```python3
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



### Binary tree
```python3
# Binary tree
axiom = "0"
rules = {"1":"11", "0":"1[+0]-0"}
iterations = 10
angle = 45
```

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/binary_tree.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/binary_tree.png)

### L-system Bush (Version 2)
```python3
# Thin Bush

axiom = "F"
rules = {"F":"FF+[+F-F-F]-[-F+F+F]"}
iterations = 4 # TOP: 6
angle = 22.5
```

[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/thin_bushes.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/Thin_bush.png)

### L-system Bush (Version 3)
```python3
# Bushes

axiom = "Y"
rules = {"X":"X[-FFF][+FFF]FX", "Y":"YFX[+Y][-Y]"}
iterations = 6 # TOP: 6
angle = 25.7
```
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/bushes.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/L_bushes.png)

# Some more interesting patterns for you!
## Vibrating-Sphere
[Code](https://github.com/rodosingh/Tesellate-2020/blob/main/Codes/vibrate_circle.py)

![](https://github.com/rodosingh/Tesellate-2020/blob/main/vibrating_sphere.png)


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

Thank you! for being with us so long. 👏🙌😊 
