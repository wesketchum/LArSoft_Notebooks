#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ROOT
import ROOT.art as art
import ROOT.gallery as gallery
import ROOT.simb as simb
import ROOT.raw as raw
from array import array

# In[2]:


# Some functions that I find useful to reduce error-prone typing.
def read_header(h):
        """Make the ROOT C++ jit compiler read the specified header."""
        ROOT.gROOT.ProcessLine('#include "%s"' % h)

def provide_get_valid_handle(klass):
        """Make the ROOT C++ jit compiler instantiate the
           Event::getValidHandle member template for template
           parameter klass."""
        ROOT.gROOT.ProcessLine('template gallery::ValidHandle<%(name)s> gallery::Event::getValidHandle<%(name)s>(art::InputTag const&) const;' % {'name' : klass})


# In[3]:


read_header('gallery/ValidHandle.h')
provide_get_valid_handle('std::vector<simb::MCTruth>')
provide_get_valid_handle('std::vector<raw::OpDetWaveform>')


# In[ ]:




