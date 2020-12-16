// Copyright (C) 2020 Intel Corporation
// SPDX-License-Identifier: Apache-2.0
//

#pragma once

#include "shared_test_classes/subgraph/range_add.hpp"

namespace SubgraphTestsDefinitions {

TEST_P(RangeAddSubgraphTest, CompareWithRefs) {
    Run();
}

TEST_P(RangeNumpyAddSubgraphTest, CompareWithRefs) {
    Run();
}

}  // namespace SubgraphTestsDefinitions
