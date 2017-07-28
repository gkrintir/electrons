#include "DataFormats/Common/interface/Ptr.h"
#include "DataFormats/Common/interface/Wrapper.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "electrons/DataFormats/interface/Electron.h"


#include <vector>
#include <map>

namespace  {
  struct dictionary {


    electrons::Electron    fgg_ele;
    edm::Ptr<electrons::Electron>   ptr_fgg_ele;
    edm::Wrapper<electrons::Electron>  wrp_fgg_ele;
    std::vector<electrons::Electron>  vec_fgg_ele;
    edm::Wrapper<std::vector<electrons::Electron> > wrp_vec_fgg_ele;




};
}
// Local Variables:
// mode:c++
// indent-tabs-mode:nil
// tab-width:4
// c-basic-offset:4
// End:
// vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
