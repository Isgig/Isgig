---
geometry: margin=30mm
---
### Q3 (6)
A particle moves around the semicircular path $C_1$ from $(0,R)$ to $(0,-R)$ and then returns to $(0,R)$ along the straight path $C_2$. During this trip, the partice is subject to the force field
$$\Large\vec{F}(\vec{r})=k(xy,-x^2)$$
where $k$ is a constant. Determine the total work done by the field on the particle in terms of $k$ and $R$.

![Graph of particle through force field](C:/Users/isaac/isgig/Files/Ass2Fig3.png){width=50%}

Work done by a force field is given by the following.
$$W=\int_{a}^{b}\vec{F}(\vec{r}(t))\cdot d\vec{r}(t)$$
$\textcolor{blue}{C_1}$ and $\textcolor{blue}{C_2}$ can be parameterized with the following.
$$
\begin{aligned}
\textcolor{blue}{C_1}&:\vec{r}_1(t)=(R\sin(\pi t),R\cos(\pi t))\,,&t\in[0,1]\\
\textcolor{blue}{C_2}&:\vec{r}_2(t)=(0,R(2t-1))\,,&t\in[0,1]
\end{aligned}
$$
So $\vec{F}(\vec{r_n}(t))\cdot d\vec{r_n}(t)$ is equal to the following.
$$\begin{aligned}
\vec{F}(\vec{r_1}(t))\cdot d\vec{r_1}(t)&=k\pi R^3\sin(\pi t)dt\\
\vec{F}(\vec{r_2}(t))\cdot d\vec{r_2}(t)&=0dt
\end{aligned}
$$
Which makes sense becuase $x=0$ along $\textcolor{blue}{C_2}$ and $\vec{F}$ has a factor of $x$ in both components.

So, the total work done by the particle is given by the following.
$$
\begin{aligned}
W&=\int_{t=0}^{1}k\pi R^3\sin(\pi t)\,dt\\
&=2kR^3
\end{aligned}
$$