//
// Created by levi on 11/12/18.
//

#include <map>

typedef int LinkID;
typedef char* config;

class PhyNeighbour
{

};

class PhyDev
{
    PhyNeighbour* getNeighbours();
    void connect(PhyNeighbour nei);
    void disconnect(PhyNeighbour nei);

    //Thread_eventListener    (for AP PhyDev)


};


class DecisionMaker
{
    std::map<PhyDev,PhyNeighbour> getConnectInstruction(std::map<PhyDev,PhyNeighbour> devNeiMap);
    void updateConfig(config newConfig);

};

class LinkController
{
    LinkID* getLinks();

    std::map<PhyDev,PhyNeighbour> getNeighbours();

    void updateLink();
    //PhyDev::getNeighbours()
    //DecisionMaker::getConnectInstruction()
    //PhyDev::disconnect() + delete Thread_linkInterface
    //PhyDev::connect() + create Thread_linkInterface
    //send Links to networkController

    void updateConfig(config newConfig,bool immediateRefresh);
    //DecisionMaker::updateConfig()
};