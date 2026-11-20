
/* =====================================
   NVIDIA NetQ Network Observability Lab
   Network Topology Module
===================================== */

window.NetQLab = window.NetQLab || {};

NetQLab.topology = [
    {
        id: "SW-01",
        name: "Core Switch",
        type: "Switch",
        status: "Online"
    },
    {
        id: "SW-02",
        name: "Distribution Switch",
        type: "Switch",
        status: "Online"
    },
    {
        id: "RTR-01",
        name: "Main Router",
        type: "Router",
        status: "Warning"
    },
    {
        id: "SRV-01",
        name: "Network Server",
        type: "Server",
        status: "Online"
    },
    {
        id: "SW-03",
        name: "Access Switch",
        type: "Switch",
        status: "Offline"
    }
];

NetQLab.getTopology = function () {
    return NetQLab.topology;
};

NetQLab.displayTopology = function () {
    console.table(NetQLab.getTopology());
};

console.log("Network topology module loaded.");
