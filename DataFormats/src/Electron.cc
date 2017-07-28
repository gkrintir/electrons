#include "electrons/DataFormats/interface/Electron.h"

using namespace electrons;

Electron::Electron() : pat::Electron()
{}

Electron::~Electron()
{}

Electron::Electron( const pat::Electron &anelectron ) : pat::Electron( anelectron )
{}

// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

