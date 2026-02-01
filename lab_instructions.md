## Lab 2c: Radius of the Earth

In the ancient times, Eratothenes estimated the radius of the Earth through geometry. He first found a known location where the sun shines directly overhead (no shadow). But at the same time in another location, a shadow forms, and he mesaured the shadow's angle. Using basic geometry, if $\theta$ is the angle between the sun rays at two locations, then:
$$
\frac{\theta}{360\degree} = \frac{D}{2\pi R}
$$
With some simple algebra, we can calculate the Radius of the Earth:
$$
R = \frac{D \cdot 360 \degree}{\theta \cdot 2 \pi }
$$

Then, using some conversions, we know that $360\degree = 2\pi$. This simplifies to the following:

$$
R = \frac{D}{\theta}
$$

Create a program that takes the distance (in km) an angle (in degrees) to estimate the radius of the earth. Have the program convert the degrees into radians using the `radians()` function from the `math` module. Print both the estimated and real radius (6,378km) and print the error. Error calculation:
$$
Error = \frac{Real - Estimated}{Real}
$$

After creating your program, test your program using the following values:
- Eratothesenes Estimations: d = 800km, $\theta = 7.2\degree$ 
- Guam To Hawaii: d $\approx$ 6126km, $\theta \approx 55.15\degree$  