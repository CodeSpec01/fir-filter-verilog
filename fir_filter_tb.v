module tb_fir_filter_4tap;

    // Clock generation
    reg clk = 0;
    always #5 clk = ~clk;

    // Input and output signals
    reg signed [15:0] in_sample = 16'sd0;
    wire signed [35:0] out_sample;

    // Instantiate the DUT (Design Under Test)
    fir_filter_weighted dut (
        .clk(clk),
        .in_sample(in_sample),
        .out_sample(out_sample)
    );

    // Input data from file
    reg signed [15:0] input_data [0:999];
    integer i;
    integer fout;

    // Initialising testbench
    initial begin

        // Load input data from file
        $readmemb("input_data.txt", input_data);
        fout = $fopen("output_data.txt", "w");

        // Check if file opened successfully
        if (!fout) begin
            $display("Error opening output file!");
            $finish;
        end

        #10;

        // Apply input samples and write output to file
        for (i = 0; i < 1000; i = i + 1) begin
            // Apply input sample
            @(posedge clk);
            in_sample <= input_data[i];

            // Wait for output to be ready
            @(posedge clk);
            $fwrite(fout, "%020b\n", out_sample);

            // Display progress every 100 samples
            if (i % 100 == 0)
                $display("Processed %0d samples", i);
        end

        // Close the output file
        $fclose(fout);
        $display("Done filtering.");
        #10 $finish;
    end

endmodule
