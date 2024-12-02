# pingscope
Measuring and graphing ping

## Round trip time tiers
|Rank|Range|Color image|Color name|Color code|
|:-:|:-:|:-:|:-:|:-:|
|S|0 - 9ms|![](https://via.placeholder.com/16/0000ff/FFFFFF/?text=%20)|Blue|#0000FF|
|A|10 - 14ms|![](https://via.placeholder.com/16/a0d8ef/FFFFFF/?text=%20)|Skyblue|#87CEEB|
|B|15 - 19ms|![](https://via.placeholder.com/16/00ff00/FFFFFF/?text=%20)|Green|#00FF00|
|C|20 - 29ms|![](https://via.placeholder.com/16/ffff00/FFFFFF/?text=%20)|Yellow|#FFFF00|
|D|30 - 49ms|![](https://via.placeholder.com/16/ee7800/FFFFFF/?text=%20)|Orange|#FFA500|
|E|50ms over|![](https://via.placeholder.com/16/ff0000/FFFFFF/?text=%20)|Red|#FF0000|

## Versions

|Version|Summary|
|:--|:--|
|0.1.0|Release pingscope|

## Installation

`pip install pingscope`

## Usage
### pingscope
![](./images/usage.png)
```python
import pingscope as ps

dst = "www.google.com"
pingFilePath = "./images/usage.ping"
ps.Pingscope().save(pingFilePath, dst)
ps.Pingscope().load(pingFilePath).to_figure_helper().write_image("./images/usage.png")
```
