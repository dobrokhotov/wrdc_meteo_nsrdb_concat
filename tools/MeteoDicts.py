#coding: utf-8
import numpy as np

N_DICT = {
    '100%.':1,
    '90  or more, but not 100%':0.95,
    '70 – 80%.':0.75,
    '60%.':0.6,
    '50%.':0.5,
    '40%.':0.4,
    '20–30%.':0.25,
    '10%  or less, but not 0':0.05,
    'no clouds':0,
    'Sky obscured by fog and/or other meteorological phenomena.':np.nan
    }


CL_DICT = {
    'Stratus fractus or Cumulus fractus of bad weather, or both (pannus), usually below Altostratus or Nimbostratus.':'St',
    'Stratocumulus cumulogenitus.':'Sc',
    'Stratocumulus other than Stratocumulus cumulogenitus.':'Sc',
    'Cumulus mediocris or congestus, with or without Cumulus of species fractus or humilis or Stratocumulus, all having their bases at the same level.':'Cu',
    'Cumulonimbus calvus, with or without Cumulus, Stratocumulus or Stratus.':'Cb',
    'Cumulonimbus capillatus (often with an anvil), with or without Cumulonimbus calvus, Cumulus, Stratocumulus, Stratus or pannus.':'Cb',
    'Cumulus and Stratocumulus other than Stratocumulus cumulogenitus, with bases at different levels.':'Sc',
    'Cumulus humilis or Cumulus fractus other than of bad weather, or both.':'Cu',
    'Stratus nebulosus or Stratus fractus other than of bad weather, or both.':'St',
    'No Stratocumulus, Stratus, Cumulus or Cumulonimbus.':np.nan,
    }


CM_DICT = {
     'Altostratus translucidus.':'As',
     'Altocumulus castellanus or floccus.':'Ac',
     'Altostratus opacus or Nimbostratus.':'As',
     'Altocumulus translucidus at a single level.':'Ac',
     'Altocumulus translucidus in bands, or one or more layers of Altocumulus translucidus or opacus, progressively invading the sky; these Altocumulus clouds':'Ac',
     'Altocumulus cumulogenitus (or cumulonimbogenitus).':'Ac',
     'Patches (often lenticular) of Altocumulus translucidus, continually changing and occurring at one or more levels.':'Ac',
     'Altocumulus translucidus or opacus in two or more layers, or Altocumulus opacus in a single layer, not progressively invading the sky, or Altocumulus with':'Ac',
     'Altocumulus of a chaotic sky, generally at several levels.':'Ac',
     'No Altocumulus, Altostratus or Nimbostratus.':np.nan
    }


CH_DICT = {
     'Cirrocumulus alone, or Cirrocumulus accompanied by Cirrus or Cirrostratus or both, but Cirrocumulus is predominant.':'Cc',
     'Cirrus fibratus, sometimes uncinus, not progressively invading the sky.':'Ci',
     'Cirrus (often in bands) and Cirrostratus, or Cirrostratus alone, progressively invading the sky; they generally thicken as a whole, but the continuous veil does not reach 45 degrees above the horizon.':'Cs',
     'Cirrus (often in bands) and Cirrostratus, or Cirrostratus alone, progressively invading the sky; they generally thicken as a whole; the continuous veil extends more than 45 degrees above the horizon, without the sky being totally covered.':'Cs',
     'Cirrus spissatus cumulonimbogenitus.':'Ci',
     'Cirrostratus covering the whole sky.':'Cs',
     'Cirrus spissatus, in patches or entangled sheaves, which usually do not increase and sometimes seem to be the remains of the upper part of a Cumulonimbus; or Cirrus castellanus or floccus.':'Ci',
     'Cirrus uncinus or fibratus, or both, progressively invading the sky; they generally thicken as a whole.':'Ci',
     'Cirrostratus not progressively invading the sky and not entirely covering it.':'Cs',
     'No Cirrus, Cirrocumulus or Cirrostratus.':np.nan
    }

RRR_DICT = {
    'No precipitation':0,
    'Trace of precipitation':0.05
    }