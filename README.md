# de_code_challenge_jan

## Context

A fictional electrical grid operator South West Grid (SWG) is responsible for 10 grid areas, in each of these areas the SWG must balance the demand and availability of electricty. When demand is high it seeks to purchase units to fill any shortfall, if demand is less than availability it will seek to sell energy back to energy suppliers.

This is done through a balancing request, when SWG notices a balancing request is necessary in a grid it will open a balancing request for the required amount of energy. When a balance request is  opened the suppliers will submit bids, not all bids are necessarily accepted and sometimes SWG cannot fill a shortfall resulting in brownouts, or cannot sell surpless energy resulting in a financial loss.

Balancing requests are generated and handled by grid monitoring devices with low computing power, the bids are submitted to these devices and an algorithm accepts or declines bids. Once daily the device will attempt to upload the data to a centralised server. Given the low computing and storage capabilities of these devices the data is uploaded as plain text files.


## Objective

In the below mountpoint you find a collection of these text files, the data in these files has a hierachy as shown in the schema below but the files themselves are flat text files with no ids linking parent and child items. Therefore the order of the lines in the text files matters as it indicates which parent item each child belongs to.

Your objective is to ingest and normalise the data into tables with one table per type of item, you should be able to reconstruct the original file by joining your tables together.


### Schema

Each line in a file begins with a three character string indicating which field that line belongs to.

Fields
- AAA  file header.

- BBB represents a balancing request being opened.

- CAA represents information about an entity making a bid related to the 
previous BBB line.

- CA1 Bid information for the bidder in the last CAA line.

- CA2 Status of the bid made in the previous CA1 line.

- CBB indicates the closing of the balancing request from the previous BBB line.

- ZZZ file footer.

Data Structure:

        AAA|date|file_id|File_name|file_start_time
        |    |
        |    |--BBB|grid_id|balancing_quantity|balance_request_time|
        |        |
        |        --CAA|grid_id|bidding_entity_name|bidding_entity_id|
        |        |    |
        |        |    --CA1|grid_id|bid_quantity|bid_time|bid_offer
        |        |    |
        |        |    --CA2|bid_id|bid_status|bid_status_time
        |        |    
        |        --CBB|grid_id|balancing_quantity|difference
        |
        ZZZ|date|file_name|file_end_time
        