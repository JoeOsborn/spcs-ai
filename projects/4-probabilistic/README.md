Individual or pair (small) assignment.

Make a probabilistic program expressing your Bayesian model from earlier today. Try to give it a prior based on your intuition, or by analyzing a dataset. Either PyMC3 or WebPPL is fine.

Submit it as an `.ipynb` or a `.wppl` file in `projects/4-probabilistic`.

Wet grass example:

```javascript
var wet = function() {
  var clouds = flip(0.2); //equivalent to "sample(Bernoulli({p:0.5}))": returns 0 or 1
  var rain = clouds ? flip(0.9) : flip(0.01);
  var sprinkler = clouds ? 0 : flip(0.5);
  var wet = (rain || sprinkler) ? 1 : 0;
  ///*chance of sprinkler and rain together */ return (rain && sprinkler) ? 1 : 0
  ///*chance of sprinkler given observed not cloudy*/ condition(clouds == 0); return sprinkler ? 1 : 0;
  ///*chance of rain and not cloudy*/  return (rain && !clouds) ? 1 : 0;
  /* chance of wet grass */ return wet;
};

viz.auto(Infer({method: 'enumerate'}, wet))
```
