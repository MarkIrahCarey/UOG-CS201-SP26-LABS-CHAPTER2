## General Instructions
Each Lab should have the following header:
```
"""
Author: Your Name
Date: Today's Date/Due Date
FileName: The File's Name
Purpose: What the program is about
"""
```

For your file names, please name each lab by the following {specificlabname}_yourlastnamethenfirstnameinitials

So for example, If I am turning in Lab 2c, the file name is `calc_earth_radius_galangmi.py`

## Lab 2a: Physics in Action! (Projectile Motion)

Think of throwing a ball as far as you can. When you release it, two things are at play
- Forward speed (how hard you throw)
- Upward angle (how high you aim)

We want to know how we can get the following:
- How high will it go?
- How long will it fly?
- How far it will go?

To calculate this, there are three things we need to look out for, displacement, velocity, and acceleration. Gravity always pulls down, so `g = -9.81m/s^2`.

Lets look at our two friends, displacement and velocity which are the following equations:

Displacement: $s(t) = s_0 + v_0t + \dfrac{1}{2}at^2$

Velocity: $v(t) = v_0 + at$

The velocities for both x and y positions are the following:

$$
\begin{align*}
v_x &= v_0\cos\theta \\
v_y &= v_0\sin\theta
\end{align*}
$$

To find our horizontal position, we know that we start at 0, so $s_0 = 0$,this also means we have no acceleration, so $a = 0$ then our starting velocity (how hard we throw) is $v_{0x} = v_0\cos\theta$. So we get for horizontal position:

$$
\begin{align*}
x(t) &= 0 + v_{0x}t + \dfrac{1}{2}(0)t^2 \\
&= (v_0\cos\theta)t
\end{align*}
$$ 

We can make the same assumptions for vertical position, but, we use sin as that relates to vertical and the acceleration is due to gravity, so we get the following

$$
\begin{align*}
y(t) &= 0 + v_{0y}t + \dfrac{1}{2}(-g)t^2 \\
&= (v_0\sin\theta)t - \dfrac{1}{2}(g)t^2
\end{align*}
$$

Using these equations, we can solve the 3 questions from earlier.

#### How high will it go?

The highest point means that our velocity reaches zero. Taking the derivative of y(t) and setting it equal to zero we get that 

$$
y'(t) = v_y = 0 = v_0\sin\theta - gt_{peak}
$$ 

So, for the time at the highest point:

$$
t_{peak} = \dfrac{v_0\sin\theta}{g}
$$

Plugging that into y(t) we get the following: 

$$
\begin{align*}
y(t_{peak}) = H &= (v_0\sin\theta)(\dfrac{v_0\sin\theta}{g}) - \dfrac{1}{2}(g)(\dfrac{v_0\sin\theta}{g})^2 \\
&\fbox{$H = \dfrac{v_0^2\sin^2\theta}{2g}$}
\end{align*}
$$

#### How long will it fly?

We know that it is no longer in the air if $y(t) = 0$. Plugging that in and solving for time (t), we get the following:

$$
\begin{align*}
0 &= (v_0\sin\theta)t - \dfrac{1}{2}gt^2 \\
0 &= t(v_0\sin\theta - \dfrac{1}{2}gt) \\
\end{align*}
$$

Then our solution for T is the 2nd:

$$
\fbox{$T = \dfrac{2v_0\sin\theta}{g}$}
$$


#### How far will it go?

The farthest point means that we have reached the max t. So simply that $x(t) = v_0\cos\theta t_{max}$

Then, since we solved for the how long this will fly, we can plug that into the equation to get the following:

$$
x(T) = \dfrac{2v_0^2\sin\theta\cos\theta}{g}
$$

Using our trig identity where $2\sin\theta\cos\theta = \sin(2\theta)$ we get:

$$
\fbox{$x(t) = \dfrac{v_0^2\sin(2\theta)}{g}$}
$$

Create a program called `projectile_calculator.py` that for any ball or projectile, asks for the initial velocity ($v_0$) and angle ($\theta$) in degrees from the user, then calculates and returns how hight the ball will fly, how long the ball will be in the air, and how far the ball will travel. Assume no air resistance and that gravity is `g = 9.81`. 

Once the program is created test it with the following values:
- $v_0 = 22, \theta = 30$ 
- $v_0 = 42.1, \theta = 45$ 

Recommended functions/operations: `math.sin`, `math.cos`, `/`, `**`
## Lab 2b: Engineering Statics

For a lot of history, bridges were build by experience. We know that thicker beams felt safer, arches felt strong, and if the bridge failed, we take the knowledge of that bridge to build a better one. We still rely on these types of instincts today, however, we turned it into math!

 When cars drive onto a bridge, we expect their weight to push down. The bridge then bends slightly. You can think of it like a ruler balanced between two table. The ruler doesn't break when pressed lightly, but if there is too much pressure, it snaps! 
 
 Same thing with the bridge, if there are a lot of cars, the bridge experiences stress. If there is too much stress, the bridge may not survive.

We will keeps things simple (totally not because your professor can't figure out how to work the math). We will assume our bridge:
- Is perfectly straight
- Is supported at both ends
- Has a uniform shape along its length
- Has cars even spread across it

This is our perfect world.

The Maximum bending stress is as follows:

$$
\sigma = \dfrac{M}{S}
$$

Where M and S are the maximum bending moment and shape strength respectively. The equations for those are the following:

$$
M = \dfrac{WL^2}{8}  \quad S = \dfrac{bh^2}{6}
$$

Where L is the length of the bridge, and W is the Load per meter given by $w = \dfrac{F}{L}$, b is the width, and h is the height. 

Then F is the total weight from all cars on the bridge given by $F = (m_{total})g$

You can represent this instead as n cars with the mass of each car, $F = (n_{total cars})(m_{mass of car})g$

If we combine all the equations you get the following for stress:

$$
\sigma = \dfrac{\dfrac{nmgL^2}{8L}}{\dfrac{bh^2}{6}}
$$

Then simplifying this, we get:

$$
\fbox{$\sigma = \dfrac{3Lnmg}{4bh^2}$}
$$

Create a program called `bridge_stress_calculator.py` that takes the input from the user for the number of cars (represented as m or mass), the length (L), width (b), and height (h) to find the max stress of a bridge. You may assume that each car is $1500kg$ and use `g = 9.81`. Have the program then print out the max stress given these parameters. 

After creating your program, do the following:
- Test using these values, $n = 67, L = 15m, b = 3m, h = 0.8m.$ The result is around $5776787.11Pa$
- Use it find out what is the max amount of cars for the underpass bridge on Guam (the one at the airport) given the following: $1,000,000 Pa$ for a bridge length of $20.4m$, width of $12m$, and a height of $5m$.

Please have the answer of cars as a comment at the end of your script.
(Note: The Following Pa is just a random number, I do not know the actual max stress of the bridge)

Recommended Functions/Operations: `/`, `()`, `*`, `**`

## Lab 2c: Radius of the Earth

In the ancient times, Eratosthenes estimated the radius of the Earth through geometry. He first found a known location where the sun shines directly overhead (no shadow). But at the same time in another location, a shadow forms, and he mesaured the shadow's angle. Using basic geometry, if $\theta$ is the angle between the sun rays at two locations, then:

$$
\frac{\theta}{360\degree} = \frac{D}{2\pi R}
$$

With some simple algebra, we can calculate the Radius of the Earth:

$$
R = \frac{D \cdot 360 \degree}{\theta \cdot 2 \pi }
$$

Then, using some conversions, we know that $360\degree = 2\pi$. This simplifies to the following:

$$
\fbox{$R_{earth} = \dfrac{D}{\theta}$}
$$

Create a program called `calc_earth_radius.py` that takes the distance (in km) an angle (in degrees) to estimate the radius of the earth. You will have to convert the degrees into radians using the `radians()` function from the `math` module in your calculations. Print both the estimated and real radius (6,378km) and print the error. Error calculation:

$$
Error = \frac{|Real - Estimated|}{Real}
$$

After creating your program, test your program using the following values:
- Test with Eratosthesenes Estimations: d = 800km, $\theta = 7.2\degree$, you shoudl get around 6366.2km, with a 0.002% error
- Approximate Guam To Hawaii: d $\approx$ 6126km, $\theta \approx 55.15\degree$  

Put the answer for Guam to Hawaii as comments at the end of your python script.

(The angle for Guam to Hawaii was calculated using [OmniCalculator](https://www.omnicalculator.com/physics/sun-angle))

Recommended Functions/Operations: `float()`, `math.radians()`, `/`, `()`


## Lab 2d
Many jobs have a standard amount of hours worked in a biweekly pay period. This is usually 80 hours. However, there are times an employee may work more hours than the standard. Either because there is low staff or the emokpyee may need extra money. For this, they will be compensated by being payed a little extra from the standard, usually in a 1.5 times rate.

Here is the breakdown, an employee's total gross pay can be calculated with the following equation:

$$
Gross Pay = (HourlyWage \cdot Regular Hours) + Overtime Pay
$$

Overtime Pay is calculated as the following:

$$
Overtime Pay = ExtraHours \cdot 1.5 \cdot HourlyWage
$$

Create a program called `employeepay.py` that takes the inputs for the hourly wage and total hours. Assume that regular hours is 80 hours and that there is always overtime hours. Have it display the normal pay, overtime pay, and gross pay.

Recommended Functions/Operations: `()`, `*`, `+`

## Lab 2e

When you eat at a restaurant, your bill includes the cost of food and drinks. But there's often an additional amount called gratuity or tip. This is a percentage of your bill that you add to thank your server for good service.

Most restaurants have this added automatically and the percent or rate can range from 10% to upwards of 22 or even 25%!

The calculations is as follows:

$$
Tip amount = Bill * (\dfrac{Gratuity}{100})
$$

Then your total bill is:

$$
Total = Bill + Tip amount
$$

Create a program called `grauity_calculator.py` that has the user enter the restaurant bill, and the Gratuity percent. Then display the tip amount from the bill, and the total bill. 

Recommended Functions/Operations: `()`, `*`, `+`
