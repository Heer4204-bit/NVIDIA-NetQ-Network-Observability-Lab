
/* =====================================
   NVIDIA NetQ Network Observability Lab
   Dashboard Analytics
===================================== */

window.NetQLab = window.NetQLab || {};

NetQLab.getDashboardStats = function () {
    const devices = NetQLab.devices || [];

    return {
        totalDevices: devices.length,
        onlineDevices: devices.filter(
            device => device.status === "Online"
        ).length,
        offlineDevices: devices.filter(
            device => device.status === "Offline"
        ).length,
        warningDevices: devices.filter(
            device => device.status === "Warning"
        ).length
    };
};

NetQLab.displayDashboardStats = function () {
    const stats = NetQLab.getDashboardStats();

    console.log("Network Dashboard Statistics");
    console.table(stats);

    return stats;
};

console.log("Dashboard analytics module loaded.");
