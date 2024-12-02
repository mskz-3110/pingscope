import pingscope as ps
import os

def write_image_sample_time(pingCount, maxCount):
  roundTripTimes = []
  for i in range(pingCount):
    roundTripTimes.append(i % 30 + 10)
  pingscope = ps.Pingscope(maxCount)
  pingscope.RoundTripTimes = roundTripTimes
  pingscope.to_figure_helper().write_image("""./images/sample_time_{}sec.png""".format(pingCount))

def test_pingscope():
  pingscope = ps.Pingscope()
  samples = {
    "./images/sample_rank_S.png": [7, 8, 9, 10, 11],
    "./images/sample_rank_A.png": [12, 13, 14, 15, 16],
    "./images/sample_rank_B.png": [17, 18, 19, 20, 21],
    "./images/sample_rank_C.png": [27, 28, 29, 30, 31],
    "./images/sample_rank_D.png": [47, 48, 49, 50, 51],
    "./images/sample_rank_E.png": [48, 49, 1000, 51, 52],
    "./images/sample_empty.png": [],
    "./images/sample_timeout.png": [1000],
  }
  for filePath in samples:
    pingscope.RoundTripTimes = samples[filePath]
    pingscope.to_figure_helper().write_image(filePath)

  write_image_sample_time(30, 30)
  write_image_sample_time(60, 60)
  write_image_sample_time(3600, 30)

def test_pingscope_usage():
  dst = os.getenv("PINGSCOPE_DST")
  if dst is not None:
    pingFilePath = "./images/usage.ping"
    ps.Pingscope().save(pingFilePath, dst)
    ps.Pingscope().load(pingFilePath).to_figure_helper().write_image("./images/usage.png")
