## Sample lab: Calculating Gravity

Every object in the universe attracts every other object with a force that depends on their masses and the distance between them. This idea, discovered by the amazing Sir Isaac Newton, shows that the same force that makes an apple fall also keeps the Moon in orbit around Earth!

This equation is written as the following:

$$
F = G\dfrac{m_1m_2}{g}
$$

Where:

$$
G(\text{Gravitational Constant}): 6.674 \cdot 10^{-11} N\cdot m^2 / kg^2 \\[1em]
m_1, m_2 (\text{Masses of the Objects}): \text{The mass of the two objects}
$$

Suppose we wanted to know the gravity of any object. To do this, the Force exterted from the object on a small mass would be:

$$
F = \dfrac{GMm}{R^2}
$$

We also know from everyday experience that gravity gives objects weight due to gravity $F = mg$, using this and the force from a planet, to find the gravity of said object:

$$
\begin{align*}
mg &= \dfrac{GMm}{R^2} \\
&\fbox{$g = \dfrac{GM}{R^2}$}
\end{align*}
$$

Create a program called `gravity_calculator.py` that grabs the Mass of the planet (or object), and the radius of the object from the user. To make it easier, we will seperate the number and power. So, have the user give the significand/coefficient and power for the mass and radius. 

So for example, $a \cdot 10^n$, we will get a the significant/coefficient, and n the power. Then calculate the gravity of that planet (or object). Round that gravity, then display the gravity.

Then after, test with these values:
Earth: $mass: 5.972 \cdot 10^{24}kg$, $radius: 6.371 \cdot 10^6m$
Saturn: $5.683 \cdot 10^{26}kg$, $5.8232 \cdot 10^7m$
Sun: $mass: 1.989 \cdot 10^{30}kg$, $1.392 \cdot 10^9m$

