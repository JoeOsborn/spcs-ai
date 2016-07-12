# The Google Self Driving Car
Google's self driving cars are developed by Google X, and are impressive autonomous vehicles which operate in line with the rules of the road. They intelligently interpret their environment and react to them by steering, accelerating, or decelerating.

The project was formerly led by Sebastian Thrun, and is developed by a team of Google engineers. It is simply an attempt to advance autonomous vehicles, and Google X is a good place to lead this research because their labs are dedicated to trying projects which at some point were considered impossible.

## Knowledge Representation
The Google Car utilizes expensive sensors to generate a 3D view of the world around it. It utilizes this information to form multiple data models of where pedestrians around it are.

Central concepts based off released information is the car's location, at all times. The team has made it clear that GPS is too inaccurate for their purposes, so it combines data from GPS and it's laser sensor to precisely determine location.

Other, more peripheral information, is likely information that it filters out. This probably includes objects on the sidewalk (such as people, dogs, people in vehicles, etc) which it predicts are not going to affect it's driving abilities.

## Interaction With Humans
The car is designed to be used by human passengers, and is meant to avoid hitting other objects while efficiently moving the passenger from point A to point B. It assumes that the human will not try to do anything in the car to alter the driving (latest revisions of the car do not include steering wheel or pedals), and it also assumes that the human will be content with preset rules of the car (max speed, route, etc).


### Malicious User Interaction
A hostile user could probably try to damage the car and steal one of the sensors (which are extremely expensive), or possibly try to weigh down the car and mess with its expectations. To injure others, a user might be able to take control of the vehicle using a steering wheel and override a decision made by the Google car. Indeed, Google claims that a few of it's accidents were caused by the driver, not the car itself. This isn't anything more than manually causing harm, but it raises doubt on the accuracy of autonomous vehicles. A hostile user from outside the car could do something that it has never experienced (and thus cannot react to), such as jumping from the sidewalk in front of the car, taping a sensor while it's stopped, or trying to drive head on into the Google car. I doubt that the Google car is prepared for any of these cases (except possibly a malfunctioning sensor).
