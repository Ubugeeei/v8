// Copyright 2018 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import { TurboshaftGraphNode } from "../phases/turboshaft-graph-phase/turboshaft-graph-node";
import { GraphNode } from "../phases/graph-phase/graph-node";
import { TurboshaftGraphBlock } from "../phases/turboshaft-graph-phase/turboshaft-graph-block";
import { GenericPosition } from "../source-resolver";

export interface ClearableHandler {
  brokeredClear(): void;
}

export interface HistoryHandler {
  showTurbofanNodeHistory(node: GraphNode, phaseName: string): void;
}

export interface NodeSelectionHandler {
  select(nodes: Iterable<TurboshaftGraphNode | GraphNode | string | number>, selected: boolean):
    void;
  clear(): void;
  brokeredNodeSelect(nodeIds: Set<string>, selected: boolean): void;
}

export interface BlockSelectionHandler {
  select(blocks: Iterable<TurboshaftGraphBlock | string | number>, selected: boolean): void;
  clear(): void;
  brokeredBlockSelect(blockIds: Array<string>, selected: boolean): void;
}

export interface InstructionSelectionHandler {
  select(instructionIds: Array<string>, selected: boolean): void;
  clear(): void;
  brokeredInstructionSelect(instructionsOffsets: Array<[number, number]> | Array<Array<number>>,
                            selected: boolean): void;
}

export interface SourcePositionSelectionHandler {
  select(sourcePositions: Array<GenericPosition>, selected: boolean): void;
  clear(): void;
  brokeredSourcePositionSelect(sourcePositions: Array<GenericPosition>, selected: boolean): void;
}

export interface RegisterAllocationSelectionHandler {
  // These are called instructionIds since the class of the divs is "instruction-id"
  select(instructionIds: Array<number>, selected: boolean): void;
  clear(): void;
  brokeredRegisterAllocationSelect(instructionsOffsets: Array<[number, number]>, selected: boolean):
    void;
}
