# sonar
A sonar based model for self-driving cars. 

It can drives the virtual car coded in this repo : 
https://github.com/tawnkramer/sdsandbox

## steps for one steering angle recommendation

- take as input a image recorded by a camera
  put at the front of the car.

- spot the pixels of the solid lines of the road, 
  with a basic color detection (this works well for 
  video game images but not for real images).
  
- compute the real coordinates of theses pixels, 
  using the cross ratio which is a projective invariant.
  See https://en.wikipedia.org/wiki/Cross-ratio. 
  
- compute the angle theta between the car and the solid
  lines. This is the recommended steering angle.


