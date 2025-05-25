@license(LGPL);

import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.networklayer.ipv4.RoutingTableRecorder;
import inet.common.misc.ThruputMeteringChannel;
import inet.node.inet.Router;
import inet.node.inet.StandardHost;
import simu5g.common.binder.Binder;
import simu5g.common.carrierAggregation.CarrierAggregation;
import simu5g.nodes.NR.NRUe;
import simu5g.nodes.Upf;
import simu5g.nodes.NR.gNodeB;
import simu5g.nodes.backgroundCell.BackgroundCell;
import simu5g.world.radio.LteChannelControl;

network ds {
    parameters:
        int numClients = default(5);
        int numBgCells = default(0);
    types:
        channel gigabitline extends ThruputMeteringChannel {
            delay = 0.01us;
            datarate = 10Gbps;
            ber = 0;
            per = 0;
            thruputDisplayFormat = 'b';
        }
    submodules:
        channelControl: LteChannelControl {
            @display("p=50,25;is=s");
        }
        routingRecorder: RoutingTableRecorder {
            @display("p=50,75;is=s");
        }
        configurator: Ipv4NetworkConfigurator {
            @display("p=50,125;is=s");
        }
        binder: Binder {
            @display("p=50,175;is=s");
        }
        carrierAggregation: CarrierAggregation {
            @display("p=50,260;is=s");
        }
        server: StandardHost {
            @display("i=device/server;p=200,100;is=s");
        }
        router: Router {
            @display("p=250,100;is=s");
        }
        upf: Upf {
            @display("p=300,100;is=s");
        }
        iUpf: Upf {
            @display("p=350,100;is=s");
        }
        gnb: gNodeB {
            @display("p=500,500;is=s");
        }
        bgCell[numBgCells]: BackgroundCell {
            @display("p=500,500;is=s");
        }
        client[numClients]: NRUe {
            @display("is=s");
        }
    connections:
        server.pppg++ <--> gigabitline <--> router.pppg++;
        router.pppg++ <--> gigabitline <--> upf.filterGate;
        upf.pppg++ <--> gigabitline <--> iUpf.pppg++;
        iUpf.pppg++ <--> gigabitline <--> gnb.ppp;
}
