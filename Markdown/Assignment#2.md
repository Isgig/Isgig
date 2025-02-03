---
title: "MATH 227 W25 Assignment #2"
author: "Isaac Giggs"
date: "February 3rd, 2025"
geometry: margin=30mm
output: html_document
---
# MATH 227 W25 Assignment #2
### Q1 (3)
An astroid is the curve (shown partially completed in red) traced out by a point on the circumference of a smaller circle rolling around the inside of a larger circle with four times the radius. If the larger circle has radius 4, then we can parametrize the astroid by $\vec{r}(t)=(4\cos^3{(t)},4\sin^3{(t)})$
Find the arc length of one quarter of the asteroid (i.e., for $0\leq t\leq \frac{\pi}{2}$)

![Graph of asteroid being traced](C:/Users/isaac/isgig/Files/Ass2Fig1.png){width=50%}

The arclength of a curve is given by the following.
$$\Large L=\int_{t=a}^b \sqrt{(x'(t))^2+(y'(t))^2}\ dt$$
Where $x$ and $y$ are their respecive components of $\vec{r}(t)$.
$$
\begin{aligned}
x(t)\hspace{2mm} &=4\cos^3(t) &\hspace{1cm} y(t)\hspace{2mm}&=4\sin^3(t)\\
x'(t)\hspace{2mm} &=12\cos^2(t)(-\sin(t)) &\hspace{1cm} y'(t)\hspace{2mm}&=12\sin^2(t)(\cos(t))\\
(x'(t))^2&=12^2\cos^4(t)(\sin^2(t)) &\hspace{1cm} (y'(t))^2&=12^2\sin^4(t)(\cos^2(t))
\end{aligned}
$$
$$
\begin{aligned}
\implies\sqrt{(x'(t))^2+(y'(t))^2}\ =&\ \sqrt{12^2\cos^4(t)\sin^2(t)+12^2\sin^4(t)\cos^2(t)}\\
=&\ \sqrt{12^2\cos^2(t)\sin^2(t)(\cos^2(t)+\sin^2(t))}\\
=&\ 12\cos(t)\sin(t)\\
=&\ 6\sin(2t)
\end{aligned}
$$
So, the arclength can be computed by integrating this function of $t$ according to the bounds of the question.
$$\underline{L}=6\int_{t=0}^{\frac{\pi}{2}}\sin(2t)\ dt\ =\ 6\left[-\frac{1}{2}\cos(2t)\right]_{t=0}^{\frac{\pi}{2}}=\underline{6}$$

### Q2 (6)
A rectangular steel wire frame with length $L$ and height $H$ (as shown) has a linear mass density (i.e., mass per unit length) given by the following.
$$\Large\rho(x,y)=\rho_0\left(\frac{2H^2-y^2}{H^2}\right)$$
Determine the total mass of the wire frame in terms of $\rho_0$, $H$, and $L$.

![Graph of wire frame](C:/Users/isaac/isgig/Files/Ass2Fig2.png){width=50%}

The total mass of the wire frame is the sum of 4 line integrals which is shown below.
$$
\begin{aligned}
\oint\limits_{\textcolor{blue}{C}}\rho(x,y)\,d\ell=&\int\limits_{(0,0)\to(L,0)}\rho(x,y)\,d\ell+\int\limits_{(L,0)\to(L,H)}\rho(x,y)\,d\ell\\
+&\int\limits_{(L,H)\to(0,H)}\rho(x,y)\,d\ell+\int\limits_{(0,H)\to(0,0)}\rho(x,y)\,d\ell
\end{aligned}
$$

Each curve can be parameterized with $t\in[0,1]$
$$
\begin{aligned}
(0,0)\to(L,0)\:&:\:\vec{r_1}(t)=(Lt,0)\\
(L,0)\to(L,H)\:&:\:\vec{r_2}(t)=(L,Ht)\\
(L,H)\to(0,H)\:&:\:\vec{r_3}(t)=(L(1-t),H)\\
(0,H)\to(0,0)\:&:\:\vec{r_4}(t)=(0,H(1-t))
\end{aligned}\hspace{15mm}
\begin{aligned}
||\vec{r_1}'(t)||dt&=Ldt\\
||\vec{r_2}'(t)||dt&=Hdt\\
||\vec{r_3}'(t)||dt&=-Ldt\\
||\vec{r_4}'(t)||dt&=-Hdt
\end{aligned}
$$
So, the total mass is computed with the following.
$$
\begin{aligned}
M&=\int_{t=0}^{1}\rho_0\left(\frac{2H^2-0^2}{H^2}\right)\,Ldt &+\int_{t=0}^{1}\rho_0\left(\frac{2H^2-H^2t^2}{H^2}\right)\,Hdt\\
&-\int_{t=0}^{1}\rho_0\left(\frac{2H^2-H^2}{H^2}\right)\,Ldt &-\int_{t=0}^{1}\rho_0\left(\frac{2H^2-H^2(1-t)^2}{H^2}\right)\,Hdt\\
&=\rho_0L
\end{aligned}
$$

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